#!/bin/python3
import contextlib, io
with contextlib.redirect_stdout(zen := io.StringIO()):
    import this
print(f"{zen.getvalue()}", end='')
