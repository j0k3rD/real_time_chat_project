#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

SERVICE_NAME = 'chatservice'

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chat_service.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

    DjangoInstrumentor().instrument()
    LoggingInstrumentor().instrument()
    RequestsInstrumentor().instrument()

    jaeger_exporter = JaegerExporter(
        agent_host_name=os.getenv("TRACING_HOST"),
        agent_port= int(os.getenv("TRACING_PORT")),
    )
    trace.set_tracer_provider(TracerProvider(
        resource=Resource.create({SERVICE_NAME: 'chatservice'})
    ))
    span_processor = BatchSpanProcessor(jaeger_exporter)
    trace.get_tracer_provider().add_span_processor(span_processor)


if __name__ == '__main__':
    main()
