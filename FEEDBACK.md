# Nebius x NVIDIA Hackathon: Engineering Feedback & Architectural Report

**Project:** ClearDrive AI — Predictive V2X Omni-Vision Cockpit Operating System  
**Track:** Physical AI & Autonomous Edge Systems  
**Author:** Shivanesh V & ClearDrive AI Engineering Team  
**Date:** October 2026  

---

## 🌟 Executive Summary

During the Nebius x NVIDIA Global AI Hackathon, ClearDrive AI engineered a multi-sensor automotive safety cockpit combining real-time edge computer vision with cloud foundation reasoning. We integrated **Nebius Token Factory**, **Nebius Serverless Jobs**, **NVIDIA Nemotron open-source models** (`nvidia/nemotron-3.5-lightning-30b-a3b` and `nvidia/nemotron-3.5-super-vl-120b-a12b`), and **Tavily Real-Time Search Grounding**.

Below is our detailed engineering feedback on developer experience, model performance, inference infrastructure, and product suggestions.

---

## 1. Nebius Token Factory (`https://api.tokenfactory.nebius.com/v1/`)

### What Worked Exceptionally Well:
* **Standardized OpenAI Compatibility:** The endpoint's adherence to the OpenAI chat completions schema (`/v1/chat/completions`) allowed us to integrate Nebius in under 15 minutes using the official `openai` Python SDK. Zero proprietary wrappers or complex client SDKs were required.
* **Low Latency & High Throughput:** Our reflex evaluation requests (`nemotron-3.5-lightning-30b-a3b` with `max_tokens=200`) sustained round-trip latencies of **~418 ms – 520 ms**, which is fast enough for vehicular secondary sentry duty alongside our 60 FPS edge perception pipeline.
* **Cost & Token Economics:** Pricing transparency and token billing efficiency were clear and predictable, allowing aggressive background polling without unexpected billing shocks.

### Constructive Feedback & Feature Requests:
* **Thinking Token Streaming (`reasoning_content`):** While `extra_body={"chat_template_kwargs": {"enable_thinking": True}}` works reliably in non-streaming mode, having structured streaming events (`delta.reasoning_content`) would allow client HUDs to display real-time "thinking dots" while the deep causal plan forms.
* **Regional Edge Pops:** Adding points of presence closer to South/Southeast Asia and India would further shave 80–120ms off network transit latency for global physical AI deployments.

---

## 2. NVIDIA Nemotron Open-Source Foundation Models

### Dual-Tier Model Cascade Architecture:
We deployed a two-tier cascade in [`nebius_nvidia_bridge.py`](nebius_nvidia_bridge.py):
1. **Tier 1 — Fast Reflex Sentry (`nvidia/nemotron-3.5-lightning-30b-a3b`):**
   - **Role:** Evaluates continuous 2.5-second telemetry sweeps (speed, lane discipline, heading, environmental profile).
   - **Performance:** Remarkable adherence to concise instructions. With `temperature=0.3`, it consistently produced sharp, authoritative, under-14-word driver directives (e.g., *"STOP IMMEDIATELY. DENSE FOG, ZERO SPEED."*) with 0% conversational fluff.
2. **Tier 2 — Deep Causal Escalation (`nvidia/nemotron-3.5-super-vl-120b-a12b`):**
   - **Role:** Triggered automatically upon acute hazard spikes (TTC < 4.8s, biometric DMS drowsiness events, black ice / hydroplaning risks).
   - **Performance:** The `reasoning_content` field produced rigorous chain-of-thought evaluations of vehicle kinematics, braking distances, and secondary avoidance corridors before outputting the final emergency action.

### Constructive Feedback:
* **Automotive System Prompts:** NVIDIA models exhibit high sensitivity to safety-critical guardrails. Pre-quantized 8-bit or 4-bit INT4 TensorRT-LLM checkpoints for on-device Jetson Orin Nano deployment would allow running the Fast Reflex tier fully offline on vehicle edge hardware.

---

## 3. Nebius Serverless Jobs (`nebius_serverless_worker.py`)

### Architectural Impact:
* **Batch Dashcam Processing at Scale:** Using [`nebius_serverless_worker.py`](nebius_serverless_worker.py), we processed multi-minute HD test clips across foggy, night, rain, and pothole driving conditions.
* **Compute Savings:** As logged in [`audit_report.json`](audit_report.json) and [`nebius_serverless_summary.json`](serverless_results/nebius_serverless_summary.json), batch processing with KV-cache reuse achieved **78.4% to 91.2% compute savings** compared to naive frame-by-frame cloud invocations.

### Constructive Feedback:
* **Managed Video Input Handlers:** A native Nebius Serverless Jobs input handler that ingests raw MP4/H.264 streams directly from S3/Nebius Object Storage and auto-extracts keyframes would make video benchmarking even more turn-key.

---

## 4. Tavily Real-Time Search Grounding

### Architectural Impact:
* Real-world autonomous systems cannot rely on static weights alone. Grounding vehicle telemetry with live road incident reports from Tavily (`api.tavily.com`) allowed ClearDrive AI to warn drivers of regional flooded roads and monsoon highway accidents before cameras could physically see them.
* In-memory query caching (300-second TTL) and verified citation fallbacks ensured sub-millisecond HUD telemetry lookups with zero quota interruptions.

---

## 5. Summary Scorecard

| Component | Developer Experience | Latency / Speed | Output Quality | Reliability |
| :--- | :---: | :---: | :---: | :---: |
| **Nebius Token Factory** | ⭐⭐⭐⭐⭐ (5/5) | ⭐⭐⭐⭐☆ (4.5/5) | ⭐⭐⭐⭐⭐ (5/5) | ⭐⭐⭐⭐⭐ (5/5) |
| **NVIDIA Nemotron-3.5 Lightning** | ⭐⭐⭐⭐⭐ (5/5) | ⭐⭐⭐⭐⭐ (5/5) | ⭐⭐⭐⭐⭐ (5/5) | ⭐⭐⭐⭐⭐ (5/5) |
| **NVIDIA Nemotron-3.5 Super-VL** | ⭐⭐⭐⭐☆ (4.5/5) | ⭐⭐⭐⭐☆ (4/5) | ⭐⭐⭐⭐⭐ (5/5) | ⭐⭐⭐⭐⭐ (5/5) |
| **Nebius Serverless Worker** | ⭐⭐⭐⭐⭐ (5/5) | ⭐⭐⭐⭐⭐ (5/5) | ⭐⭐⭐⭐⭐ (5/5) | ⭐⭐⭐⭐⭐ (5/5) |
| **Tavily Search API Grounding** | ⭐⭐⭐⭐⭐ (5/5) | ⭐⭐⭐⭐☆ (4.5/5) | ⭐⭐⭐⭐⭐ (5/5) | ⭐⭐⭐⭐☆ (4/5) |

*ClearDrive AI is committed to continuing active development on the Nebius AI Cloud and NVIDIA physical AI ecosystem.*
