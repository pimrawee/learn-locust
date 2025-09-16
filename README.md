# 🦗 Load Testing with Locust

[Locust](https://locust.io) is an open-source, Python-based load testing tool that makes it easy to define user behavior in code — no need for complex XML or GUI-based test definitions. With Locust, you can simulate millions of concurrent users to test the performance and scalability of your system.
 
> 🎥 Playlist is [learning](https://www.youtube.com/playlist?list=PLJ9A48W0kpRKMCzJARCObgJs3SinOewp5).

---

## ✨ Features at a Glance

- **🧠 Code-Driven User Behavior**  
  Write user flows and tasks using pure Python (`HttpUser`, `@task`, etc.) — highly readable, reusable, and maintainable.

- **⚖️ Distributed & Scalable**  
  Locust supports master-worker architecture to scale across multiple machines and simulate millions of virtual users.

- **🌐 Beautiful Web UI**  
  Monitor and control tests via an intuitive web interface: start/stop tests, view live stats, errors, and charts.

- **📦 TaskSet & SequentialTaskSet**  
  Group tasks logically or enforce execution order for complex flows using `TaskSet` or `SequentialTaskSet`.

- **⏳ Realistic Wait Times**  
  Simulate user "think time" using functions like `between(min, max)`, `constant(seconds)`, or `constant_pacing(seconds)`.

- **🖥️ Headless CLI Mode**  
  Run tests from the command line with full control: number of users, spawn rate, host, duration, and report formats (HTML/CSV).

- **✅ Response Validation**  
  Validate response content and status codes. Use assertions or custom logic to mark requests as passed/failed.

- **🏷️ Tag-Based Task Filtering**  
  Organize tasks using tags and selectively run them via CLI — ideal for modular testing.

- **🔁 Dynamic Correlation**  
  Extract and reuse dynamic data (e.g., session tokens, IDs) using regex, JSON, or HTML parsing for end-to-end test flows.

- **📂 Data Parameterization**  
  Load input from CSV files or generate dynamic data to simulate diverse and realistic user interactions.

- **📌 Setup & Teardown Hooks**  
  Use `on_start` and `on_stop` to define actions like login/logout at the start/end of a user session.

- **📋 Event Hooks**  
  Extend Locust by hooking into lifecycle events like `test_start`, `test_stop`, `request`, `user_error`, etc.

- **🪵 Logging Support**  
  Uses Python's built-in logging — configure levels, formats, and output destinations for full traceability.

- **⚙️ Flexible Configuration**  
  Configure Locust via Python, `.conf` files, environment variables, or command-line arguments — with CLI taking precedence.

- **🐳 Docker Support**  
  Run Locust in Docker containers for easy portability, CI/CD integration, and scalable distributed testing.

- **⚖️ Weighted Task Execution**  
  Use `@task(weight)` to assign relative frequencies to tasks for more realistic user simulation.

---

## 🚀 Installation

Make sure you have **Python 3.6+** installed, then run:

```bash
pip install locust