import logging
import pybreaker
from django.http import HttpResponse

class UserListener(pybreaker.CircuitBreakerListener):
    """
    Listener used by circuit breakers that execute chat operations.
    """

    def before_call(self, cb, func, *args, **kwargs):
        """
        Called before the circuit breaker `cb` calls `func`.
        """
        print("before_call")

    def state_change(self, cb, old_state, new_state):
        """
        Called when the circuit breaker `cb` state changes.
        """
        print("state_change")

    def failure(self, cb, exc):
        if isinstance(exc, pybreaker.CircuitBreakerError):
            # Si la excepción es del tipo pybreaker.CircuitBreakerError, activamos el estado de falla
            cb.fail(exc)  # fail() y trip () al parecer no funcionan en esta version de pybreaker. TODO: Revisar en la documentación por una alternativa o tratar de arreglarlo
            return HttpResponse("El servicio no está disponible en este momento, por favor intente más tarde.")

    def success(self, cb):
        """
        Called when a function invocation succeeds.
        """
        print("success")

class LogListener(pybreaker.CircuitBreakerListener):
    """
    Listener used to log circuit breaker events."
    """
    def state_change(self, cb, old_state, new_state):
        msg = "State Change: CB: {0}, New State: {1}".format(cb.name, new_state)
        logging.info(msg)