# Put your app in here.
from flask import Flask, request
import operations 

app = Flask(__name__)


@app.route("/add")
def calc_add():
    """Adds a and b and returns result as the body."""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(operations.add(a, b))


@app.route("/sub")
def calc_sub():
    """Subtracts b from a"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(operations.sub(a, b))


@app.route("/mult")
def calc_mult():
    """Subtracts b from a"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(operations.mult(a, b))


@app.route("/div")
def calc_div():
    """Divides a by b"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(operations.div(a, b))


OPS = {
    "add": operations.add,
    "sub": operations.sub,
    "mult": operations.mult,
    "div": operations.div
}

@app.route("/math/<operation>")
def calc_by_operation(operation):
    a = int(request.args.get("a", 2))
    b = int(request.args.get("b", 2))
    return str(OPS[operation](a, b))

