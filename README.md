# Polarization-Quantum_Anology
Light Polarization 3D Simulator is an interactive web-based physics simulation designed to model, visualize, and analyze the behavior of light polarization using Jones Calculus. Built with Three.js and Plotly.js, the application provides a dynamic 3D rendering environment alongside real-time data plotting and optical matrix calculations.
# Light Polarization 3D Simulator

An interactive web-based physics simulator designed to model, visualize, and analyze the behavior of light polarization using **Jones Calculus**. 

Built with **Three.js** and **Plotly.js**, this tool provides a dynamic 3D rendering environment, interactive optical path management, real-time data plotting, and optical matrix calculations.

![Simulator Screenshot](Screenshot.webp)

---

## Features

- **Interactive 3D Visualization:** Real-time 3D rendering of light propagation, electric field ($E$-field) vectors, and polarization envelopes built with Three.js. Includes full camera orbit controls and interactive manipulation of optical elements.
- **Dynamic Optical Path Builder:** Add, modify, rotate, and reorder optical elements along the optical axis, including:
  - Linear Polarizers ($\theta$)
  - Half-Wave Plates (HWP) & Quarter-Wave Plates (QWP)
  - General Linear & Arbitrary Birefringent Waveplates
  - Mirrors (including double-pass beam configurations)
  - Faraday Rotators ($\theta_{\text{rot}}$)
- **Jones Calculus Engine:** Employs standard Jones matrices with the phase convention $\phi = kz - \omega t$ to calculate polarization transformations, phase shifts, and state vectors $[E_x, E_y]$ across every stage of the setup.
- **Real-Time Data & Plotting:** Interactive plots displaying spatial intensity distributions along the optical axis ($z$) using Plotly.js, along with real-time polarization ellipse metrics.
- **Setup Import / Export:** Save and load custom optical path configurations using XML files.
- **Customizable Environment:** Toggle between light/dark 3D canvas themes, switch visual overlay elements ($E$-field vectors, envelope curves, labels), and animate light wave propagation.

---

## Project Structure

```text
.
├── index.html            # Landing / Introduction page
├── polarization.html      # Main 3D Simulator application page
├── intro_style.css       # Stylesheet for the intro page
├── style.css             # Main application stylesheet
├── script.js             # Core simulation logic & Jones calculus engine
├── interactiveCanvas.js  # Three.js 3D scene, rendering, & drag interactions
├── complex.min.js        # Complex number math library
├── Screenshot.webp       # Preview screenshot image
└── LICENSE               # MIT License
```

---

## Getting Started

No installation, complex build tools, or web server setup required!

1. Clone or download this repository to your local machine:
   ```bash
   git clone https://github.com/your-username/polarization-simulator.git
   ```
2. Open `index.html` or `polarization.html` directly in any modern web browser (Chrome, Firefox, Edge, Safari).

---

## Tech Stack

- **HTML5 / CSS3 / JavaScript (ES6+)**
- **[Three.js](https://threejs.org/)** - 3D WebGL rendering & CSS2DRenderer
- **[Plotly.js](https://plotly.com/javascript/)** - Interactive intensity plotting
- **[Complex.js](https://github.com/infusion/Complex.js/)** - Complex arithmetic operations
- **[Font Awesome](https://fontawesome.com/)** - UI iconography

---

## License

This project is open-source and available under the [MIT License](LICENSE).
