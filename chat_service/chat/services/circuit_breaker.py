import logging
import pybreaker

class ChatListener(pybreaker.CircuitBreakerListener):
    """
    Listener used by circuit breakers that execute chat operations.
    """

    def before_call(self, cb, func, *args, **kwargs):
        """
        Called before the circuit breaker `cb` calls `func`.
        """
        pass

    def state_change(self, cb, old_state, new_state):
        """
        Called when the circuit breaker `cb` state changes.
        """
        print("Circuit breaker state change from %s to %s" % (old_state, new_state))

    def failure(self, cb, exc):
        """
        Called when a function invocation raises a system error.
        """
        print("Error: ", exc)
        print("Error count: ", cb.fail_counter)

    def success(self, cb):
        """
        Called when a function invocation succeeds.
        """
        pass

#class LogListener(pybreaker.CircuitBreakerListener):
#    """
#    Listener used to log circuit breaker events."
#    """
#    def state_change(self, cb, old_state, new_state):
#        msg = "State Change: CB: {0}, New State: {1}".format(cb.name, new_state)
#        logging.info(msg)