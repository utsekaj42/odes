#
# odes - Extra ode integrators
#

class CVODESolveException(Exception):
    """Base class for exceptions raised by `CVODE.validate_flags`."""
    def __init__(self, soln):
        self.soln = soln
        self.args = (self._message.format(soln),)

class CVODESolveFailed(CVODESolveException):
    """`CVODE.solve` failed to reach endpoint"""
    _message = (
        "Solver failed with flag {0.flag} and finished at {0.errors.t}"
        "with values {0.errors.y}."
    )

class CVODESolveFoundRoot(CVODESolveException):
    """`CVODE.solve` found a root"""
    _message = "Solver found a root at {0.roots.t[0]}."

class CVODESolveReachedTSTOP(CVODESolveException):
    """`CVODE.solve` reached the endpoint specified by tstop."""
    _message = "Solver reached tstop at {0.tstop.t[0]}."
