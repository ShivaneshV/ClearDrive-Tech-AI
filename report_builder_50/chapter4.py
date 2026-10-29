"""
Chapter 4: Iterative Design and Methodology (Pages 19 to 28 - Exactly 10 Pages)
ClearDrive AI: Real-Time ADAS and Vision Restoration for Adverse Driving Conditions
"""

from reportlab.platypus import Paragraph, Spacer, Table, TableStyle, PageBreak, HRFlowable
from reportlab.lib import colors
from report_builder_50.styles import (
    USABLE_WIDTH, COLOR_PRIMARY, COLOR_SECONDARY, COLOR_BORDER,
    create_callout_box
)


def get_chapter4_flowables(styles):
    """Returns flowables for Chapter 4 (Pages 19 to 28 - Exactly 10 Pages)."""
    f = []

    # =========================================================================
    # PAGE 19: CHAPTER 4 COVER & 4.1 SYSTEM ARCHITECTURE
    # =========================================================================
    f.append(Paragraph("<b>CHAPTER 4</b>", styles['ChapterHeader']))
    f.append(Paragraph("<b>ITERATIVE DESIGN AND DEVELOPMENT</b>", styles['DocTitle']))
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
    # PAGE 20: 4.2 ITERATION 1 - THE BASELINE SEQUENTIAL ENGINE
    # =========================================================================
    f.append(Paragraph("<b>4.2 Iteration 1: The Baseline Sequential Engine</b>", styles['SectionHeader']))
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
    # PAGE 21: 4.3 ITERATION 1 FAILURE ANALYSIS: THE 1.8 FPS STALL
    # =========================================================================
    f.append(Paragraph("<b>4.3 Iteration 1 Failure Analysis: The 1.8 FPS Stall and Memory Crash</b>", styles['SectionHeader']))
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
    f.append(Paragraph(
        "<b>3. Catastrophic Frame Rate Collapse:</b> Even when image resolution was aggressively downsampled to $320 \\times 240$, the system achieved a maximum "
        "throughput of only <b>1.8 FPS</b>. At 1.8 FPS, the blind distance between successive frames exceeds 12.3 meters at 80 km/h, completely violating AIS-145 safety standards.",
        styles['AcademicBody']
    ))
    f.append(Spacer(1, 4))
    f.append(create_callout_box(
        "Iteration 1 Post-Mortem Conclusion",
        "Classical Soft Matting is fundamentally unsuitable for real-time edge robotics. Synchronous monolithic pipelines cannot meet automotive deadlines. "
        "The architecture required a complete mathematical and concurrency paradigm shift.",
        styles
    ))
    f.append(PageBreak())

    # =========================================================================
    # PAGE 22: 4.4 ITERATION 2 - PARALLELIZATION & ALGORITHMIC REFINEMENT
    # =========================================================================
    f.append(Paragraph("<b>4.4 Iteration 2: Parallelization & Algorithmic Refinement</b>", styles['SectionHeader']))
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
    f.append(Paragraph(
        "<b>2. Architectural Decoupling via Multi-Threading:</b> The pipeline was split into two independent concurrent threads using Python's `threading` module:<br/>"
        "• <i>Video Capture &amp; Ingestion Thread:</i> Continuously reads raw frames from the camera hardware at 30 FPS, dumping the latest frame into a shared double-buffer "
        "and discarding stale frames to permanently eradicate buffer bloat.<br/>"
        "• <i>Perception &amp; Restoration Thread:</i> Continuously grabs the freshest available frame, applies the Fast Guided Filter dehazing pipeline, and generates "
        "the real-time MJPEG broadcast stream.",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "<b>Performance Leap:</b> Iteration 2 achieved an immediate throughput surge, reaching <b>42.5 FPS</b> on x86 hardware and <b>22.4 FPS</b> on the Raspberry Pi 4B. "
        "System RAM consumption dropped from 3.4 GB to a lean <b>142 MB</b>. The engineering team appeared to have solved the latency crisis.",
        styles['AcademicBody']
    ))
    f.append(Spacer(1, 4))
    f.append(create_callout_box(
        "Iteration 2 Milestone Achievement",
        "Throughput increased by 2,300% (from 1.8 FPS to 42.5 FPS). Latency per frame dropped below the 33.3 ms automotive threshold for the first time. "
        "However, road testing revealed subtle, insidious optical defects.",
        styles
    ))
    f.append(PageBreak())

    # =========================================================================
    # PAGE 23: 4.5 ITERATION 2 FAILURE MODES: THE 'TREE BUG' & FLICKERING
    # =========================================================================
    f.append(Paragraph("<b>4.5 Iteration 2 Failure Modes: The 'Tree Bug' and Atmospheric Flickering</b>", styles['SectionHeader']))
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
    # PAGE 24: 4.6 ITERATION 3 - PRODUCTION OMNIVISION ARCHITECTURE
    # =========================================================================
    f.append(Paragraph("<b>4.6 Iteration 3: Production OmniVision Architecture</b>", styles['SectionHeader']))
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
    # PAGE 25: 4.7 ITERATION 3 - GYROSCOPIC STABILIZATION & HORIZON DAMPENER
    # =========================================================================
    f.append(Paragraph("<b>4.7 Iteration 3: Inertial Gyroscopic Stabilization & Adaptive Horizon</b>", styles['SectionHeader']))
    f.append(Paragraph(
        "Physical road vehicles are subject to continuous high-frequency vibration, chassis pitch during acceleration/braking, and sharp vertical shocks "
        "when traversing potholes or expansion joints. When a monocular camera vibrates, two severe failures occur: (1) visual motion blur degrades edge detection, "
        "and (2) the optical horizon line $y_{horizon}$ oscillates, causing calculated obstacle distances $Z$ to fluctuate wildly by up to $\\pm 40\\%$.",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "<b>Dual 1D Projection Correlation Stabilizer:</b> To stabilize incoming frames without the prohibitive latency of full 2D optical flow (e.g., Lucas-Kanade "
        "or Farneback, which require 15-25 ms), ClearDrive AI introduces a sub-millisecond <b>Dual 1D Projection Correlation Dampener</b>. "
        "Each incoming frame is collapsed along its horizontal and vertical axes into two 1D intensity projection vectors:",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "$$P_y(y) = \\sum_{x=1}^{W} I(x, y), \\quad P_x(x) = \\sum_{y=1}^{H} I(x, y)$$",
        styles['MathEquation']
    ))
    f.append(Paragraph(
        "Vertical chassis displacement $\\Delta y$ between consecutive frames is determined by locating the maximum cross-correlation peak of $P_y(y)$ via Fast Fourier "
        "Transforms (FFT). Because 1D FFTs across vectors of length 720 require only $O(H \\log H)$ operations, vertical displacement is computed in an astonishing "
        "<b>0.38 milliseconds</b>. The image is then counter-shifted via sub-pixel affine translation.",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "<b>Adaptive Horizon Dampener:</b> The calibrated optical horizon $y_{horizon}$ used in the pinhole distance formula is continuously updated via an inertial "
        "dampening filter: $y_{horizon}^{(t)} = y_{horizon}^{(t-1)} + \\beta_{gyro} \\cdot \\Delta y$, where $\\beta_{gyro} = 0.12$. This ensures that calculated "
        "obstacle distances $Z$ and Time-to-Collision (TTC) metrics remain rock-steady even when driving over rough mountain cobblestones.",
        styles['AcademicBody']
    ))
    f.append(PageBreak())

    # =========================================================================
    # PAGE 26: 4.8 ITERATION 3 - AR LANES & POTHOLE DEPTH HAZARD MAPPING
    # =========================================================================
    f.append(Paragraph("<b>4.8 Iteration 3: AR Dynamic Lane Guidance & Pothole Hazard Mapping</b>", styles['SectionHeader']))
    f.append(Paragraph(
        "Under adverse weather conditions, human drivers struggle to perceive roadway boundaries and road surface hazards. Iteration 3 integrates two "
        "complementary structural perception modules directly into the OmniVision pipeline:",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "<b>1. Augmented Reality (AR) Dynamic Lane Projection:</b> To guide drivers through dense fog and blinding rain, ClearDrive AI projects a high-contrast, "
        "semi-transparent neon-cyan navigation carpet onto the asphalt ahead. The lane detection engine operates in four stages:<br/>"
        "• <i>Trapezoidal Perspective ROI:</i> Isolates the forward drivable corridor, rejecting off-road mountain cliff faces, billboards, and the sky.<br/>"
        "• <i>Adaptive Gradient Thresholding:</i> Computes directional horizontal Sobel gradients ($|G_x| &gt; T_x$) to isolate longitudinal white/yellow lane markings.<br/>"
        "• <i>Probabilistic Hough Transform &amp; Slope Filtering:</i> Extracts line segments, rejecting horizontal lines and retaining valid road angles ($|m| \\in [0.4, 2.5]$).<br/>"
        "• <i>Temporal Kalman Smoothing:</i> Left and right lane boundaries are tracked across frames via a linear Kalman filter, preventing visual jitter when lane paint is partially missing.",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "<b>2. Color-Coded Pothole Depth Hazard Mapping:</b> Potholes on Indian roads represent severe physical hazards capable of causing fatal rollovers. "
        "ClearDrive AI segments asphalt craters using morphological top-hat and black-hat operators within the rectified roadway corridor. "
        "Crucially, to prevent false positives from fallen tree leaves and organic roadside debris, candidates pass through an <b>HSV Vegetation Rejection Filter</b> "
        "($Hue \\in [35^\\circ, 85^\\circ]$ is discarded). Craters are dynamically color-coded by estimated depth and collision risk:",
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
    # PAGE 27: 4.9 ITERATION 3 - ZERO-LIGHT GHOST-VISION & ANTI-GLARE
    # =========================================================================
    f.append(Paragraph("<b>4.9 Iteration 3: Zero-Light 'Ghost-Vision' & Polarized Anti-Glare</b>", styles['SectionHeader']))
    f.append(Paragraph(
        "Nighttime driving on unlit rural highways and dual-carriageway corridors presents two opposite photometric extremes: pitch-black darkness and blinding high-beam glare. "
        "Iteration 3 resolves both extremes through specialized digital signal processing modules:",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "<b>1. Starlight HDR 'Ghost-Vision' Mode:</b> When ambient illumination drops below 1.0 lux, standard dashcams produce near-black frames filled with sensor noise. "
        "ClearDrive AI activates Ghost-Vision DSP:<br/>"
        "• <i>YUV Chrominance Decoupling:</i> The frame is converted to YUV space. Chrominance channels ($U, V$) are frozen to prevent the severe color shifting typical of RGB equalization.<br/>"
        "• <i>Black Pedestal Noise Suppression:</i> A small pedestal value ($Y_{pedestal} = 12$) is subtracted to suppress CMOS sensor thermal dark current noise.<br/>"
        "• <i>Dual-Tile Adaptive CLAHE:</i> The luminance channel $Y$ is equalized across an $8 \\times 8$ contextual grid with clip limit $\\alpha_{clip} = 2.5$, "
        "followed by a global logarithmic tone curve that elevates deep shadows without blowing out midtones.<br/>"
        "• <i>Unsharp Masking:</i> A $3 \\times 3$ Laplacian kernel sharpens edges, revealing unlit pedestrians, stray cattle, and road barriers hundreds of meters ahead.",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "<b>2. Polarized Anti-Glare Shield:</b> When oncoming vehicles flash aftermarket high-beam LED headlights, sensor photodiodes saturate, causing blooming. "
        "ClearDrive AI applies a non-linear specular knee compression rolloff function:",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "$$I_{out} = \\begin{cases} I_{in}, & I_{in} < T_{knee} \\\\ T_{knee} + (255 - T_{knee}) \\cdot \\left(\\frac{I_{in} - T_{knee}}{255 - T_{knee}}\\right)^{\\gamma}, & I_{in} \\ge T_{knee} \\end{cases}$$",
        styles['MathEquation']
    ))
    f.append(Paragraph(
        "where $T_{knee} = 215$ and compression exponent $\\gamma = 0.45$. Blinding high-beam flares are compressed into soft halos, preserving full visibility of the road ahead.",
        styles['AcademicBody']
    ))
    f.append(PageBreak())

    # =========================================================================
    # PAGE 28: 4.10 MATHEMATICAL FORMULATIONS & CONVERGENCE PROOFS
    # =========================================================================
    f.append(Paragraph("<b>4.10 Unified Mathematical Formulations of Iteration 3</b>", styles['SectionHeader']))
    f.append(Paragraph(
        "The mathematical foundations governing the unified ClearDrive AI OmniVision perception engine are synthesized below:",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "<b>Equation 4.1 (Koschmieder Radiance Restoration with Adaptive Floor &amp; EMA Airlight):</b>",
        styles['SubsectionHeader']
    ))
    f.append(Paragraph(
        "$$\\hat{\\mathbf{J}}(x) = \\frac{\\mathbf{I}(x) - \\mathbf{A}_{smooth}^{(t)}}{\\max\\left(t_{FGF}(x), \\; t_0(x)\\right)} + \\mathbf{A}_{smooth}^{(t)}, \\quad t_0(x) = \\max\\left(0.15, \\; \\sigma(Y(x)/32) \\cdot 0.35\\right)$$",
        styles['MathEquation']
    ))
    f.append(Paragraph(
        "<b>Equation 4.2 (Fast Guided Filter Subsampled Linear Coefficients):</b>",
        styles['SubsectionHeader']
    ))
    f.append(Paragraph(
        "$$a_k = \\frac{\\frac{1}{|\\omega|} \\sum_{i \\in \\omega_k} I_i p_i - \\mu_k \\bar{p}_k}{\\sigma_k^2 + \\epsilon}, \\quad b_k = \\bar{p}_k - a_k \\mu_k, \\quad q_i = \\bar{a}_i I_i + \\bar{b}_i$$",
        styles['MathEquation']
    ))
    f.append(Paragraph(
        "<b>Equation 4.3 (Monocular Pinhole Ground Distance &amp; Dynamic Time-to-Collision):</b>",
        styles['SubsectionHeader']
    ))
    f.append(Paragraph(
        "$$Z_k = \\frac{f_y \\cdot H_{cam}}{y_{bottom, k} - y_{horizon}^{(t)}}, \\quad TTC_k = \\frac{Z_k}{v_{relative}} = \\frac{Z_k}{\\frac{Z_k^{(t - \\Delta t)} - Z_k^{(t)}}{\\Delta t}}$$",
        styles['MathEquation']
    ))
    f.append(Paragraph(
        "<b>Equation 4.4 (MediaPipe 3D Eye Aspect Ratio &amp; Psychomotor PERCLOS):</b>",
        styles['SubsectionHeader']
    ))
    f.append(Paragraph(
        "$$EAR = \\frac{\\|p_{160} - p_{144}\\| + \\|p_{158} - p_{153}\\|}{2 \\cdot \\|p_{33} - p_{133}\\|}, \\quad PERCLOS = \\frac{1}{N_{win}} \\sum_{n=1}^{N_{win}} \\mathbb{I}(EAR_n < 0.21)$$",
        styles['MathEquation']
    ))
    f.append(Spacer(1, 2))
    f.append(create_callout_box(
        "Mathematical Convergence and Stability Guarantee",
        "By enforcing Lyapunov stability through first-order EMA on airlight $\\mathbf{A}$ and strictly bounding transmission $t(x) \\ge t_0(x) &gt; 0$, "
        "the radiance reconstruction operator $\\hat{\\mathbf{J}}(x)$ is mathematically guaranteed against numerical singularities and unbounded gradient explosions.",
        styles
    ))
    f.append(PageBreak())

    return f
