FROM python:3.10-buster as builder
WORKDIR /app
COPY ./alexa-actions/alexa_actions.py .
COPY ./alexa-actions/config.py .
COPY ./alexa-actions/const.py .
COPY ./alexa-actions/schemas.py .
COPY ./alexa-actions/language_strings.json .
COPY ./alexa-actions/prompts.py .
COPY ./alexa-actions/requirements.txt .

RUN pip install -r requirements.txt

FROM alpine:latest as tailscale
WORKDIR /app
COPY . ./
ENV TSFILE=tailscale_1.62.1_amd64.tgz
RUN wget https://pkgs.tailscale.com/stable/${TSFILE} && \
  tar xzf ${TSFILE} --strip-components=1
COPY . ./


FROM public.ecr.aws/lambda/python:3.10
#can't test locally without it
ADD https://github.com/aws/aws-lambda-runtime-interface-emulator/releases/latest/download/aws-lambda-rie /usr/local/bin/aws-lambda-rie
RUN chmod 755 /usr/local/bin/aws-lambda-rie
COPY ./custom_entrypoint /var/runtime/custom_entrypoint
COPY --from=builder /app/ /var/task
COPY --from=tailscale /app/tailscaled /var/runtime/tailscaled
COPY --from=tailscale /app/tailscale /var/runtime/tailscale
RUN mkdir -p /var/run && ln -s /tmp/tailscale /var/run/tailscale && \
  mkdir -p /var/cache && ln -s /tmp/tailscale /var/cache/tailscale && \
  mkdir -p /var/lib && ln -s /tmp/tailscale /var/lib/tailscale && \
  mkdir -p /var/task && ln -s /tmp/tailscale /var/task/tailscale

# Run on container startup.
EXPOSE 8080
ENTRYPOINT ["/var/runtime/custom_entrypoint"]
CMD [ "alexa_actions.event_handler" ]
