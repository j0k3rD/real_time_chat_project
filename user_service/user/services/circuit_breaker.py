from decouple import config
from django.shortcuts import redirect
import pybreaker


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
        """
        Called when a function invocation raises a system error.
        """
        print("failure")
        url = config("USER_URL")
        return redirect(url + "/error/")

    def success(self, cb):
        """
        Called when a function invocation succeeds.
        """
        print("success")