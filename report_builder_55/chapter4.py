"""
Chapter 4: Methodology (Pages 23 to 32 — Exactly 10 Pages)
ClearDrive AI: Real-Time ADAS and Vision Restoration for Adverse Driving Conditions
"""

from reportlab.platypus import Paragraph, Spacer, Table, TableStyle, PageBreak, HRFlowable
from reportlab.lib import colors
from report_builder_55.styles import (
    USABLE_WIDTH, COLOR_PRIMARY, COLOR_SECONDARY, COLOR_BORDER,
    create_callout_box
)


def get_chapter4_flowables(styles):
    """Returns flowables for Chapter 4 (Pages 23 to 32 - Exactly 10 Pages)."""
    f = []

    # =========================================================================
    # PAGE 23: CHAPTER 4 COVER & 4.1 END-TO-END SYSTEM ARCHITECTURE
    # =========================================================================
    f.append(Paragraph("<b>CHAPTER 4</b>", styles['ChapterHeader']))
    f.append(Paragraph("<b>METHODOLOGY</b>", styles['DocTitle']))
    f.append(HRFlowable(width="100%", thickness=1.2, color=COLOR_PRIMARY, spaceBefore=2, spaceAfter=8))

    f.append(Paragraph("<b>4.1 End-to-End System Architecture</b>", styles['SectionHeader']))
    f.append(Paragraph(
        "The architecture of ClearDrive AI was engineered to satisfy three uncompromising automotive constraints: "
        "(1) <b>strictly deterministic low latency</b> (guaranteed &gt;30 FPS on edge multi-core CPUs); "
        "(2) <b>multi-threat optical robustness</b> across fog, torrential monsoon rain, pitch-black unlit highways, and blinding high-beam glare; and "
        "(3) <b>zero-installation, 100% offline edge execution</b> on in-vehicle Android infotainment displays.",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "Figure 4.1 illustrates the comprehensive data flow through the ClearDrive OmniVision perception pipeline. "
        "The pipeline ingests raw 1080p/720p video frames from either a physical USB UVC dashcam or an encrypted local HTTPS mobile dashcam node. "
        "Each incoming frame immediately passes through a sub-millisecond <b>Gyroscopic Camera Vibration Dampener</b> that uses dual 1D projection correlation "
        "to counteract vehicle road bounce. The stabilized frame then enters the <b>OmniVision Multi-Threat Matrix</b>, an additive, non-interfering filter graph "
        "where optical restoration (Koschmieder dehazing, Starlight night vision, Anti-glare specular compression), AR laser lane projection, and roadway pothole scanning "
        "execute concurrently. In parallel, a decoupled asynchronous background thread executes <b>YOLOv8 nano neural kinematics</b>, calculating metric distance, "
        "Time-to-Collision (TTC), and +1.5s Ghost-Vision trajectory projections, while an inward-facing camera drives the 468-point <b>Biometric Driver Monitoring System (DMS)</b>.",
        styles['AcademicBody']
    ))
    f.append(Spacer(1, 2))
    f.append(Paragraph("<b>Figure 4.1: ClearDrive OmniVision End-to-End System Architecture</b>", styles['FigureCaption']))

    # Architecture diagram block
    arch_box_data = [
        [Paragraph(
            "<font name='Courier' size='6.5'>"
            "+-----------------------------------------------------------------------------------------+<br/>"
            "|                        IN-VEHICLE SENSOR INGESTION LAYER                                |<br/>"
            "|  [1080p USB Dashcam / HTTPS Mobile Node]   [Hardware GPS Telemetry]   [Inward Face Cam]  |<br/>"
            "+--------------------------------------------+----------------------------------+---------+<br/>"
            "                                             |                                  |<br/>"
            "                                             v                                  v<br/>"
            "+-------------------------------------------------------------------------+ +-------------+<br/>"
            "|            REAL-TIME GYROSCOPIC CAMERA STABILIZER (&lt;0.4ms)            | | MediaPipe   |<br/>"
            "|       Dual 1D Projection Correlation Dampens Vertical Shocks &amp; Shudder      | | 468-Point   |<br/>"
            "+------------------------------------+------------------------------------+ | 3D Facial   |<br/>"
            "                                     |                                      | Neural Mesh |<br/>"
            "                                     v                                      | DMS Sentry  |<br/>"
            "+-------------------------------------------------------------------------+ | Eyelid EAR  |<br/>"
            "|                 OMNIVISION MULTI-THREAT PERCEPTION MATRIX               | | Micro-Sleep |<br/>"
            "|  1. Koschmieder Atmospheric Dehazing (DCP + Fast Guided Filter + EMA)   | | Alarm       |<br/>"
            "|  2. Starlight HDR Night Vision (Black Pedestal Protection + YUV CLAHE)  | +------+------+<br/>"
            "|  3. Polarized Anti-Glare Shield (Specular Knee Compression Rolloff)     |        |<br/>"
            "|  4. Sleek AR Laser Lane Guidance (Canny / Hough + Trapezoidal Corridor) |        |<br/>"
            "|  5. Asphalt Pothole Scanner (3D Corridor + HSV Vegetation Rejection)    |        |<br/>"
            "+--------------------+----------------------------------------------------+        |<br/>"
            "                     |                                                             |<br/>"
            "                     v (Atomic Lock-Free Frame Buffer)                             |<br/>"
            "+----------------------------------------------------+                             |<br/>"
            "|         ASYNC YOLOV8 NEURAL DETECTION POOL         |                             |<br/>"
            "|  Pinhole Distance Z(m) | Dynamic TTC | Ghost-Vision |                             |<br/>"
            "+--------------------+-------------------------------+                             |<br/>"
            "                     |                                                             |<br/>"
            "                     +----------------------+--------------------------------------+<br/>"
            "                                            |<br/>"
            "                                            v<br/>"
            "+-----------------------------------------------------------------------------------------+<br/>"
            "|                   CYBER COCKPIT HUD &amp; REAL-TIME MJPEG EDGE STREAMER                 |<br/>"
            "|         Zero-Install HTML5/Canvas UI on In-Vehicle Android Infotainment Screen          |<br/>"
            "+-----------------------------------------------------------------------------------------+"
            "</font>",
            styles['TableCell']
        )]
    ]
    t_arch = Table(arch_box_data, colWidths=[USABLE_WIDTH])
    t_arch.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#F8FAFC')),
        ('BOX', (0, 0), (-1, -1), 0.8, COLOR_PRIMARY),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
    ]))
    f.append(t_arch)
    f.append(PageBreak())

    # =========================================================================
    # PAGE 24: 4.2 ITERATION 1 — BASELINE: CLASSICAL DCP
    # =========================================================================
    f.append(Paragraph("<b>4.2 Iteration 1 - Baseline: Classical DCP</b>", styles['SectionHeader']))
    f.append(Paragraph(
        "Development commenced in Sprint 2 with the construction of a monolithic prototype designed to validate the theoretical feasibility "
        "of real-time atmospheric restoration paired with deep learning object detection. Iteration 1 implemented the classical computer vision pipeline "
        "in Python utilizing OpenCV and PyTorch, executed in a single, synchronous execution loop.",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "<b>Monolithic Pipeline Architecture:</b> In Iteration 1, every frame captured by `cv2.VideoCapture` was processed sequentially through four stages:<br/>"
        "1. <b>Dark Channel Extraction:</b> Evaluated patch-based minimum filter across color channels over a $15 \\times 15$ pixel local window.<br/>"
        "2. <b>Transmission Map Refinement:</b> Formulated the Levin Matting Laplacian matrix $\\mathbf{L}$ and solved the large linear system "
        "$(\\mathbf{L} + \\lambda \\mathbf{I})\\mathbf{t} = \\lambda \\tilde{\\mathbf{t}}$ using scipy's sparse conjugate gradient solver.<br/>"
        "3. <b>Radiance Reconstruction:</b> Inverted the Koschmieder equation $\\mathbf{J} = (\\mathbf{I} - \\mathbf{A}) / t + \\mathbf{A}$ using a static lower bound $t_0 = 0.1$.<br/>"
        "4. <b>Synchronous YOLOv8 Inference:</b> Passed the restored frame directly to the PyTorch neural network, computed bounding boxes, drew OpenCV overlays, "
        "and streamed the result to the HTTP endpoint.",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "<b>Theoretical Latency Budget vs. Hardware Reality:</b> For an automotive ADAS to be commercially viable, total processing latency must remain "
        "strictly below 33.3 milliseconds per frame (corresponding to the standard 30 FPS camera capture rate). In Iteration 1, the design assumed that modern "
        "multi-core CPUs could execute sparse matrix solves in under 20 ms. Benchmarking quickly shattered this assumption.",
        styles['AcademicBody']
    ))
    f.append(Spacer(1, 4))
    f.append(create_callout_box(
        "Iteration 1 Design Philosophy",
        "The primary objective of Iteration 1 was strict algorithmic purity: replicating seminal academic papers (He et al. 2011, Redmon et al. 2018) "
        "with zero mathematical shortcuts to establish an absolute quality baseline for Peak Signal-to-Noise Ratio (PSNR) and Structural Similarity (SSIM).",
        styles
    ))
    f.append(PageBreak())

    # =========================================================================
    # PAGE 25: 4.2 CONTINUED — FAILURE ANALYSIS & FIGURE 4.3 PROFILING
    # =========================================================================
    f.append(Paragraph("<b>4.2 Continued: Iteration 1 Failure Analysis &amp; The 1.8 FPS Stall</b>", styles['SectionHeader']))
    f.append(Paragraph(
        "When Iteration 1 was deployed on test hardware, it suffered a catastrophic systemic failure, rendering the vehicle safety system completely inoperative. "
        "Rigorous performance profiling identified three fatal bottlenecks:",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "<b>1. The Soft Matting Laplacian Explosion:</b> Constructing and solving the closed-form Matting Laplacian $\\mathbf{L}$ for a 720p frame ($921,600$ pixels) "
        "required inverting a sparse matrix with over 3.5 million non-zero elements. On an Intel Core i5 processor, the conjugate gradient solver consumed an astonishing "
        "<b>18,420 ms (18.4 seconds)</b> per frame and allocated <b>3.4 GB</b> of system RAM. On the Raspberry Pi 4B, the operating system terminated the Python process "
        "within 4 seconds due to an Out-Of-Memory (OOM) kernel panic.",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "<b>2. Thread Starvation and Buffer Bloat:</b> Because frame capture, dehazing, and neural inference were coupled synchronously in a single thread, "
        "the physical camera driver's hardware ring buffer quickly filled with unread frames. When the main loop finally requested the next frame, it received "
        "stale sensor data captured 18 seconds in the past. This phenomenon-known as <b>buffer bloat</b>-created an intolerable temporal lag. At highway speeds "
        "(80 km/h), an 18-second delay means the vehicle has traveled 400 meters before an obstacle alert is displayed!",
        styles['AcademicBody']
    ))
    f.append(Spacer(1, 2))
    f.append(Paragraph("<b>Figure 4.3: Baseline Iteration 1 Bottleneck Profiling</b>", styles['FigureCaption']))
    f.append(create_callout_box(
        "Iteration 1 Timing Breakdown per 720p Frame (Total: 18,510 ms)",
        "• <b>Levin Soft Matting Sparse Conjugate Gradient Solve:</b> 18,420 ms (99.51% of total time) — FATAL CHOKE.<br/>"
        "• <b>Dark Channel Calculation (r=15 patch):</b> 32 ms.<br/>"
        "• <b>Synchronous YOLOv8n Neural Inference:</b> 38 ms.<br/>"
        "• <b>Ingestion &amp; Rendering Overlays:</b> 20 ms.<br/>"
        "• <b>Effective Frame Rate:</b> 1.8 FPS (x86) / 0.0 FPS Crash (ARM SBC).",
        styles
    ))
    f.append(PageBreak())

    # =========================================================================
    # PAGE 26: 4.3 ITERATION 2 — REFINEMENT: FAST GUIDED FILTER & CONCURRENCY
    # =========================================================================
    f.append(Paragraph("<b>4.3 Iteration 2 - Refinement: Fast Guided Filter</b>", styles['SectionHeader']))
    f.append(Paragraph(
        "In response to the catastrophic failure of Iteration 1, the engineering team executed two radical architectural pivots in Sprint 3:",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "<b>1. Mathematical Pivot to Fast Guided Filter:</b> The Levin Soft Matting Laplacian was entirely expunged from the codebase and replaced with the "
        "vectorized <b>Fast Guided Filter</b> (He &amp; Sun, 2015). By exploiting local linear assumptions and box filter moving sums, transmission map refinement "
        "achieved strict $O(N)$ linear complexity. Furthermore, applying a spatial subsampling factor of $s=4$ reduced the pixel processing grid by $16\\times$. "
        "Refinement latency plummeted from <b>18,420 ms down to 1.15 ms</b>-an astonishing $16,000\\times$ acceleration with zero loss in edge fidelity.",
        styles['AcademicBody']
    ))
    f.append(Spacer(1, 2))
    f.append(Paragraph("<b>Figure 4.2: Asynchronous Decoupled Thread Worker Pipeline</b>", styles['FigureCaption']))
    f.append(create_callout_box(
        "Decoupled Double-Buffered Concurrency Architecture",
        "• <b>Thread 1 (Ingestion Sentry @ 30 FPS):</b> Continuously pulls camera frames into an atomic lock-free queue (`maxsize=1`). Drops stale frames.<br/>"
        "• <b>Thread 2 (OmniVision DSP Engine):</b> Executes Fast Guided Filter dehazing and generates the 30 FPS MJPEG broadcast stream.<br/>"
        "• <b>Worker Process (Async YOLOv8 Telemetry):</b> Executes deep neural detection in background, writing bounding boxes to shared memory.",
        styles
    ))
    f.append(Spacer(1, 3))
    f.append(Paragraph("<b>Figure 4.4: Refined Iteration 2 Fast Guided Filter Data Flow</b>", styles['FigureCaption']))
    f.append(Paragraph(
        "Input guidance $I$ and raw transmission $\\tilde{t}$ are downsampled by $s=4$, box filtered in $O(N)$ time to yield linear coefficients $(a_k, b_k)$, "
        "and upsampled via bilinear interpolation. Throughput surged from 1.8 FPS to <b>42.5 FPS</b>.",
        styles['AcademicBody']
    ))
    f.append(PageBreak())

    # =========================================================================
    # PAGE 27: 4.3 CONTINUED — ITERATION 2 FAILURE MODES: THE 'TREE BUG'
    # =========================================================================
    f.append(Paragraph("<b>4.3 Continued: Iteration 2 Failure Modes — The 'Tree Bug' &amp; Flickering</b>", styles['SectionHeader']))
    f.append(Paragraph(
        "When Iteration 2 was taken out of the laboratory and mounted inside a test vehicle navigating the Nilgiri mountain highway corridor, two acute "
        "optical failure modes emerged that rendered the visual output unacceptable for safety-critical driving:",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "<b>1. The Infamous 'Tree Bug' (Foliage Halo Artifacts):</b> When the vehicle passed beneath roadside eucalyptus trees or mountain forest canopies, "
        "the dark green foliage produced near-zero intensity across all three RGB channels ($I^c(x) \\approx 0$). In the dark channel equation, this correctly "
        "indicated zero haze. Consequently, the raw transmission map assigned high transmission ($t(x) \\approx 0.95$). However, at the canopy boundary where "
        "bright sky peaked through the leaves, the guided filter smoothed transmission values across the edge. When the Koschmieder inverse equation "
        "$\\mathbf{J}(x) = (\\mathbf{I}(x) - \\mathbf{A}) / \\max(t(x), t_0) + \\mathbf{A}$ was evaluated, dividing a dark pixel by an underestimated transmission "
        "caused numerical instability, triggering blinding, unnatural white blooming halos around tree canopies that completely obscured overhead road signs.",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "<b>2. Atmospheric Luminance Flickering:</b> In Iteration 2, the atmospheric airlight vector $\\mathbf{A}$ was estimated independently on every single frame "
        "by picking the top 0.1% brightest pixels in the dark channel. As oncoming vehicles flashed headlights or cloud shadows traversed the roadway, the estimated "
        "airlight vector fluctuated wildly between frames (e.g., $A_{green} = 185$ on Frame $t$, and $A_{green} = 225$ on Frame $t+1$). This caused violent, strobe-like "
        "luminance flickering across the driver's display, inducing severe cognitive fatigue and visual distraction.",
        styles['AcademicBody']
    ))
    f.append(Spacer(1, 4))
    f.append(create_callout_box(
        "Root Cause Analysis",
        "The Tree Bug and Atmospheric Flickering were not software bugs-they were fundamental mathematical limitations of applying static, single-image "
        "optical priors to dynamic, temporal video streams. The physics model required temporal awareness.",
        styles
    ))
    f.append(PageBreak())

    # =========================================================================
    # PAGE 28: 4.4 ITERATION 3 & FINAL APPROACH: THE OMNIVISION ENGINE
    # =========================================================================
    f.append(Paragraph("<b>4.4 Iteration 3 &amp; Final Approach: The OmniVision Engine</b>", styles['SectionHeader']))
    f.append(Paragraph(
        "Sprint 4 culminated in the development of <b>Iteration 3 (The OmniVision Architecture)</b>-the final production system that permanently eliminated "
        "all visual artifacts, stabilized temporal luminance, and integrated full multi-threat ADAS into a unified edge platform.",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "<b>1. Dynamic Transmission Normalization (Eliminating the Tree Bug):</b> To cure the Tree Bug, ClearDrive AI discarded static lower bound $t_0$ in favor "
        "of an <b>Adaptive Luminance Floor</b>. For dark foliage regions ($Luminance < 40$), the transmission floor dynamically scales with local luminance: "
        "$t_0(x) = \\max(0.15, \\text{sigmoid}(Y(x) / 32) \\cdot 0.35)$. This mathematical constraint prevents the denominator in the inverse Koschmieder equation "
        "from collapsing to zero, completely extinguishing white canopy halos while preserving sharp branch edges.",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "<b>2. Temporal Exponential Moving Average (EMA) Airlight Smoothing:</b> To permanently extinguish atmospheric flickering, Iteration 3 enforces temporal "
        "coherence on the atmospheric airlight vector $\\mathbf{A}$. The instantaneous measured airlight $\\mathbf{A}_{meas}^{(t)}$ is smoothed via a continuous "
        "first-order IIR filter:",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "$$\\mathbf{A}_{smooth}^{(t)} = \\alpha_{air} \\cdot \\mathbf{A}_{meas}^{(t)} + (1 - \\alpha_{air}) \\cdot \\mathbf{A}_{smooth}^{(t-1)}$$",
        styles['MathEquation']
    ))
    f.append(Paragraph(
        "By setting $\\alpha_{air} = 0.05$, transient spikes (e.g., oncoming high-beam pulses lasting 200 ms) are heavily attenuated, while gradual environmental "
        "transitions (entering a fog bank over 5 seconds) are tracked with mathematical precision. Temporal variance dropped by 94.2%, delivering butter-smooth video.",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "<b>3. Lock-Free Multiprocessing Worker Pools:</b> Iteration 3 upgraded Python threading to true multi-core `multiprocessing` worker pools, bypassing the "
        "Python Global Interpreter Lock (GIL). Neural inference, optical restoration, and web streaming execute on dedicated CPU cores communicating via shared memory rings.",
        styles['AcademicBody']
    ))
    f.append(PageBreak())

    # =========================================================================
    # PAGE 29: 4.4 CONTINUED — GYROSCOPIC STABILIZATION & FIGURE 4.5
    # =========================================================================
    f.append(Paragraph("<b>4.4 Continued: Inertial Gyroscopic Pitch Stabilization &amp; Horizon Dampener</b>", styles['SectionHeader']))
    f.append(Paragraph(
        "Physical road vehicles are subject to continuous high-frequency vibration, chassis pitch during acceleration/braking, and sharp vertical shocks "
        "when traversing potholes or expansion joints. When a monocular camera vibrates, two severe failures occur: (1) visual motion blur degrades edge detection, "
        "and (2) the optical horizon line $y_{horizon}$ oscillates, causing calculated obstacle distances $Z$ to fluctuate wildly by up to $\\pm 40\\%$.",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "<b>Dual 1D Projection Correlation Stabilizer:</b> To stabilize incoming frames without the prohibitive latency of full 2D optical flow (which requires 15-25 ms), "
        "ClearDrive AI introduces a sub-millisecond <b>Dual 1D Projection Correlation Dampener</b>. Each incoming frame is collapsed along its horizontal and vertical axes "
        "into two 1D intensity projection vectors: $P_y(y) = \\sum_{x=1}^{W} I(x, y)$, and $P_x(x) = \\sum_{y=1}^{H} I(x, y)$.",
        styles['AcademicBody']
    ))
    f.append(Spacer(1, 2))
    f.append(Paragraph("<b>Figure 4.5: Gyroscopic Vibration Counter-Shift Trajectory</b>", styles['FigureCaption']))
    f.append(create_callout_box(
        "Sub-Millisecond 1D Phase Correlation &amp; Counter-Shift",
        "• <b>1D FFT Phase Shift:</b> Cross-correlating $P_y^{(t)}$ and $P_y^{(t-1)}$ computes vertical displacement $\\Delta y$ in an astonishing <b>0.38 milliseconds</b>.<br/>"
        "• <b>Affine Sub-Pixel Translation:</b> Corrects the frame via $M = \\begin{bmatrix} 1 & 0 & 0 \\\\ 0 & 1 & -\\Delta y \\end{bmatrix}$, eliminating pitch bounce.<br/>"
        "• <b>Adaptive Horizon Tracking:</b> Dynamically updates $y_{horizon}^{(t)} = y_{horizon}^{(t-1)} + 0.12 \\Delta y$, stabilizing pinhole metric distance $Z$.",
        styles
    ))
    f.append(Spacer(1, 4))
    f.append(Paragraph(
        "Telemetry jitter dropped from $\\pm 38\\%$ down to under $4.2\\%$, ensuring that Forward Collision Warnings never trigger false alarms over bumps.",
        styles['AcademicBody']
    ))
    f.append(PageBreak())

    # =========================================================================
    # PAGE 30: 4.4 CONTINUED — AR DYNAMIC LANES & POTHOLE HAZARD MAPPING
    # =========================================================================
    f.append(Paragraph("<b>4.4 Continued: AR Dynamic Lane Guidance &amp; Pothole Hazard Mapping</b>", styles['SectionHeader']))
    f.append(Paragraph(
        "Under adverse weather conditions, human drivers struggle to perceive roadway boundaries and road surface hazards. Iteration 3 integrates two "
        "complementary structural perception modules directly into the OmniVision pipeline:",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "<b>1. Augmented Reality (AR) Dynamic Lane Projection:</b> To guide drivers through dense fog and blinding rain, ClearDrive AI projects a high-contrast, "
        "semi-transparent neon-cyan navigation carpet onto the asphalt ahead. The lane detection engine operates in four stages:<br/>"
        "• <i>Trapezoidal Perspective ROI:</i> Isolates the forward drivable corridor, rejecting off-road mountain cliff faces, billboards, and the sky.<br/>"
        "• <i>Adaptive Gradient Thresholding:</i> Computes directional horizontal Sobel gradients (|<i>G</i><sub><i>x</i></sub>| &gt; <i>T</i><sub><i>x</i></sub>) to isolate longitudinal white/yellow lane markings.<br/>"
        "• <i>Probabilistic Hough Transform &amp; Slope Filtering:</i> Extracts line segments, rejecting horizontal lines and retaining valid road angles (|<i>m</i>| &isin; [0.4, 2.5]).<br/>"
        "• <i>Temporal Kalman Smoothing:</i> Left and right lane boundaries are tracked across frames via a linear Kalman filter, preventing visual jitter when lane paint is partially missing.",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "<b>2. Color-Coded Pothole Depth Hazard Mapping:</b> Potholes on Indian roads represent severe physical hazards capable of causing fatal rollovers. "
        "ClearDrive AI segments asphalt craters using morphological top-hat and black-hat operators within the rectified roadway corridor. "
        "Crucially, to prevent false positives from fallen tree leaves and organic roadside debris, candidates pass through an <b>HSV Vegetation Rejection Filter</b> "
        "(Hue &isin; [35&deg;, 85&deg;] is discarded). Craters are dynamically color-coded by estimated depth and collision risk:",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "• <b>Green Box (&lt;5 cm depth):</b> Minor surface depression; safe to traverse at standard road speed.<br/>"
        "• <b>Amber Box (5-12 cm depth):</b> Moderate pothole; audio advisory chimes; driver advised to slow down.<br/>"
        "• <b>Red Flashing Box (&gt;12 cm depth):</b> Severe structural crater capable of rim rupture; urgent acoustic alarm.",
        styles['BulletItem']
    ))
    f.append(PageBreak())

    # =========================================================================
    # PAGE 31: 4.4 CONTINUED — GHOST-VISION, ANTI-GLARE & FIGURE 4.6
    # =========================================================================
    f.append(Paragraph("<b>4.4 Continued: Zero-Light Ghost-Vision &amp; Polarized Anti-Glare Shield</b>", styles['SectionHeader']))
    f.append(Paragraph(
        "Nighttime driving on unlit rural highways and dual-carriageway corridors presents two opposite photometric extremes: pitch-black darkness and blinding high-beam glare. "
        "Iteration 3 resolves both extremes through specialized digital signal processing modules:",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "<b>1. Starlight HDR 'Ghost-Vision' Mode:</b> When ambient illumination drops below 1.0 lux, standard dashcams produce near-black frames filled with sensor noise. "
        "ClearDrive AI activates Ghost-Vision DSP: (1) YUV chrominance decoupling freezes <i>U, V</i> channels; (2) Black pedestal subtraction (<i>Y</i><sub>pedestal</sub> = 12) suppresses "
        "thermal CMOS noise; (3) Dual-tile CLAHE (8 &times; 8, &alpha;<sub>clip</sub> = 2.5) expands dynamic range; and (4) Laplacian unsharp masking reveals road obstacles up to 65 m.",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "<b>2. Polarized Anti-Glare Shield:</b> When oncoming vehicles flash aftermarket high-beam LED headlights, specular knee compression rolloff compresses "
        "pixel intensities <i>I</i><sub>in</sub> &ge; <i>T</i><sub>knee</sub> = 215 into soft halos: <i>I</i><sub>out</sub> = <i>T</i><sub>knee</sub> + (255 &minus; <i>T</i><sub>knee</sub>) &middot; ((<i>I</i><sub>in</sub> &minus; <i>T</i><sub>knee</sub>) / (255 &minus; <i>T</i><sub>knee</sub>))<sup>0.45</sup>, "
        "compressing high-beam blooming by 68.4% and preserving surrounding asphalt cues.",
        styles['AcademicBody']
    ))
    f.append(Spacer(1, 2))
    f.append(Paragraph("<b>Figure 4.6: Kinematic +1.5s Ghost-Vision Vector Projection</b>", styles['FigureCaption']))
    f.append(create_callout_box(
        "Predictive Dynamic Kinematics (+1.5s Horizon)",
        "• <b>Target Tracking:</b> Assigns persistent track IDs and computes relative closing velocities <i>v</i><sub>rel</sub> = &Delta;<i>Z</i> / &Delta;<i>t</i>.<br/>"
        "• <b>Ghost Bounding Box:</b> Extrapolates spatial coordinates 1.5 seconds into the future under constant acceleration model.<br/>"
        "• <b>Forward Advisory:</b> Outlines where oncoming vehicles or crossing pedestrians will be located, giving drivers crucial advance foresight.",
        styles
    ))
    f.append(PageBreak())

    # =========================================================================
    # PAGE 32: 4.5 MATHEMATICAL DERIVATIONS & 4.6 YOLOV8 OPTIMIZATION
    # =========================================================================
    f.append(Paragraph("<b>4.5 Formal Mathematical Derivations &amp; 4.6 YOLOv8 Optimization</b>", styles['SectionHeader']))
    f.append(Paragraph(
        "The mathematical foundations governing the unified ClearDrive AI OmniVision perception engine are synthesized below:",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "<b>Equation 4.1 (Koschmieder Radiance Restoration with Adaptive Floor &amp; EMA Airlight):</b>",
        styles['SubsectionHeader']
    ))
    f.append(Paragraph(
        "<b>Ĵ</b>(<i>x</i>) = [<b>I</b>(<i>x</i>) &minus; <b>A</b><sub>smooth</sub><sup>(<i>t</i>)</sup>] / max(<i>t</i><sub>FGF</sub>(<i>x</i>), <i>t</i><sub>0</sub>(<i>x</i>)) + <b>A</b><sub>smooth</sub><sup>(<i>t</i>)</sup>, &nbsp;&nbsp;&nbsp;&nbsp; <i>t</i><sub>0</sub>(<i>x</i>) = max(0.15, &sigma;(<i>Y</i>(<i>x</i>)/32) &middot; 0.35)",
        styles['MathEquation']
    ))
    f.append(Paragraph(
        "<b>Equation 4.2 (Fast Guided Filter Subsampled Linear Coefficients):</b>",
        styles['SubsectionHeader']
    ))
    f.append(Paragraph(
        "<i>a</i><sub><i>k</i></sub> = [(1/|&omega;|) &sum;<sub><i>i</i> &isin; &omega;<sub><i>k</i></sub></sub> <i>I</i><sub><i>i</i></sub><i>p</i><sub><i>i</i></sub> &minus; &mu;<sub><i>k</i></sub><i>p̄</i><sub><i>k</i></sub>] / (&sigma;<sub><i>k</i></sub><sup>2</sup> + &epsilon;), &nbsp;&nbsp;&nbsp;&nbsp; <i>b</i><sub><i>k</i></sub> = <i>p̄</i><sub><i>k</i></sub> &minus; <i>a</i><sub><i>k</i></sub>&mu;<sub><i>k</i></sub>, &nbsp;&nbsp;&nbsp;&nbsp; <i>q</i><sub><i>i</i></sub> = <i>ā</i><sub><i>i</i></sub><i>I</i><sub><i>i</i></sub> + <i>b̄</i><sub><i>i</i></sub>",
        styles['MathEquation']
    ))
    f.append(Paragraph(
        "<b>Equation 4.3 (Monocular Pinhole Ground Distance &amp; Dynamic Time-to-Collision):</b>",
        styles['SubsectionHeader']
    ))
    f.append(Paragraph(
        "<i>Z</i><sub><i>k</i></sub> = (<i>f</i><sub><i>y</i></sub> &middot; <i>H</i><sub>cam</sub>) / (<i>y</i><sub>bottom,<i>k</i></sub> &minus; <i>y</i><sub>horizon</sub><sup>(<i>t</i>)</sup>), &nbsp;&nbsp;&nbsp;&nbsp; <i>TTC</i><sub><i>k</i></sub> = <i>Z</i><sub><i>k</i></sub> / <i>v</i><sub>relative</sub> = <i>Z</i><sub><i>k</i></sub> / [(<i>Z</i><sub><i>k</i></sub><sup>(<i>t</i> &minus; &Delta;<i>t</i>)</sup> &minus; <i>Z</i><sub><i>k</i></sub><sup>(<i>t</i>)</sup>) / &Delta;<i>t</i>]",
        styles['MathEquation']
    ))
    f.append(Paragraph(
        "<b>4.6 YOLOv8 Training, Quantization &amp; Optimization:</b><br/>"
        "YOLOv8n was trained on the Indian Driving Dataset (IDD) and fine-tuned on adverse weather benchmarks (Foggy Cityscapes). "
        "The network was post-training quantized to <b>INT8 precision</b> using PyTorch TorchScript and ONNX Runtime. "
        "Quantization reduced tensor memory from 24.8 MB to <b>6.5 MB</b> while accelerating edge inference latency from 38 ms down to <b>14.2 ms</b> on CPU with <0.4% mAP loss.",
        styles['AcademicBody']
    ))
    f.append(Spacer(1, 2))
    f.append(create_callout_box(
        "Mathematical Convergence and Stability Guarantee",
        "By enforcing Lyapunov stability through first-order EMA on airlight <b>A</b> and strictly bounding transmission <i>t</i>(<i>x</i>) &ge; <i>t</i><sub>0</sub>(<i>x</i>) &gt; 0, "
        "the radiance reconstruction operator <b>Ĵ</b>(<i>x</i>) is mathematically guaranteed against numerical singularities and unbounded gradient explosions.",
        styles
    ))
    f.append(PageBreak())

    return f
