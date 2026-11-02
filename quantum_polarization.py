import os, sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import http.server, socketserver, webbrowser

P = np.pi
s = AerSimulator()

def k(n):
    q = QuantumCircuit(1, 1)
    if n == "H": pass
    elif n == "V": q.x(0)
    elif n == "D": q.h(0)
    elif n == "A": q.x(0); q.h(0)
    elif n == "R": q.h(0); q.s(0)
    elif n == "L": q.h(0); q.sdg(0)
    return q

def j(t):
    c = np.cos(t)
    s = np.sin(t)
    return np.array([[c, -s], [s, c]])

def h(a):
    t = a * P / 180
    c = np.cos(2 * t)
    s = np.sin(2 * t)
    return np.array([[c, s], [s, -c]])

def w(a):
    t = a * P / 180
    c = np.cos(t)
    s = np.sin(t)
    return np.array([[c * c + 1j * s * s, (1 - 1j) * c * s],
                     [(1 - 1j) * c * s, s * s + 1j * c * c]])

def v(n):
    m = {"H": np.array([1, 0]), "V": np.array([0, 1]),
         "D": np.array([1, 1]) / np.sqrt(2), "A": np.array([1, -1]) / np.sqrt(2),
         "R": np.array([1, -1j]) / np.sqrt(2), "L": np.array([1, 1j]) / np.sqrt(2)}
    return m[n]

def r(q, n=1024):
    q2 = q.copy()
    q2.measure(0, 0)
    t = s.run(q2, shots=n).result()
    c = t.get_counts()
    return c

def d(st, e=None):
    u = v(st)
    if e:
        for x in e:
            if x[0] == "HWP": u = h(x[1]) @ u
            elif x[0] == "QWP": u = w(x[1]) @ u
    i = np.abs(u[0])**2 + np.abs(u[1])**2
    a = np.linspace(0, 2 * P, 100)
    x = np.real(u[0] * np.exp(1j * a))
    y = np.real(u[1] * np.exp(1j * a))
    f, (a1, a2) = plt.subplots(1, 2, figsize=(10, 4))
    a1.plot(x, y, "b-", linewidth=2)
    a1.set_xlim(-1.2, 1.2)
    a1.set_ylim(-1.2, 1.2)
    a1.set_aspect("equal")
    a1.set_xlabel("Ex")
    a1.set_ylabel("Ey")
    a1.set_title(f"Polarization Ellipse |{st}>")
    a1.grid(True, alpha=0.3)
    a1.axhline(y=0, color="k", linewidth=0.5)
    a1.axvline(x=0, color="k", linewidth=0.5)
    q = k(st)
    if e:
        for x in e:
            if x[0] == "HWP": q.rz(2 * x[1] * P / 180, 0)
            elif x[0] == "QWP": q.rz(x[1] * P / 180, 0)
    c = r(q)
    l = list(c.keys())
    b = [c.get(x, 0) for x in l]
    a2.bar(l, b, color=["#2196F3", "#FF5722"])
    a2.set_xlabel("State")
    a2.set_ylabel("Counts")
    a2.set_title(f"Quantum Measurement |{st}>")
    plt.tight_layout()
    o = f"polarization_{st}.png"
    plt.savefig(o, dpi=150, bbox_inches="tight")
    plt.close()
    return u, i, o

def m():
    g = ["H", "V", "D", "A", "R", "L"]
    f, ax = plt.subplots(2, 3, figsize=(12, 8))
    for i, n in enumerate(g):
        u = v(n)
        a = np.linspace(0, 2 * P, 100)
        x = np.real(u[0] * np.exp(1j * a))
        y = np.real(u[1] * np.exp(1j * a))
        r2 = i // 3
        c = i % 3
        ax[r2][c].plot(x, y, "b-", linewidth=2)
        ax[r2][c].set_xlim(-1.2, 1.2)
        ax[r2][c].set_ylim(-1.2, 1.2)
        ax[r2][c].set_aspect("equal")
        ax[r2][c].set_title(f"|{n}>")
        ax[r2][c].grid(True, alpha=0.3)
        ax[r2][c].axhline(y=0, color="k", linewidth=0.5)
        ax[r2][c].axvline(x=0, color="k", linewidth=0.5)
    plt.suptitle("Polarization States", fontsize=14, fontweight="bold")
    plt.tight_layout()
    plt.savefig("all_states.png", dpi=150, bbox_inches="tight")
    plt.close()

if __name__ == "__main__":
    os.chdir(getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__))))
    print("Generating polarization state plots...")
    m()
    for n in ["H", "V", "D", "R"]:
        u, i, o = d(n)
        print(f"|{n}>: Jones=[{u[0]:.3f}, {u[1]:.3f}], I={i:.3f}, saved={o}")
    print("\nHWP at 22.5 deg on |H>:")
    u, i, o = d("H", [("HWP", 22.5)])
    print(f"  Jones=[{u[0]:.3f}, {u[1]:.3f}], I={i:.3f}")
    print("\nQWP at 45 deg on |H>:")
    u, i, o = d("H", [("QWP", 45)])
    print(f"  Jones=[{u[0]:.3f}, {u[1]:.3f}], I={i:.3f}")
    print("\nQWP at 45 deg then HWP at 22.5 deg on |V>:")
    u, i, o = d("V", [("QWP", 45), ("HWP", 22.5)])
    print(f"  Jones=[{u[0]:.3f}, {u[1]:.3f}], I={i:.3f}")
    p = 8000
    g = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", p), g) as z:
        print(f"\nServing at http://localhost:{p}")
        print(f"Open http://localhost:{p}/polarization.html")
        webbrowser.open(f"http://localhost:{p}/polarization.html")
        try:
            z.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")
            sys.exit(0)
