"""
Chapter 4 Builder for ClearDrive Tech PBL Report
Generates Pages 41 to 56: Iterative Design and Engineering Methodology
4.1 End-to-End System Architecture
4.2 Iteration 1 — Baseline: Classical DCP & Latency Bottlenecks
4.3 Iteration 2 — Refinement: Fast Guided Filter & The 'Tree Bug'
4.4 Iteration 3 & Final Approach: The OmniVision Engine
4.5 Formal Mathematical Derivations & Algorithmic Formulations
4.6 YOLOv8 Training, Quantization, and Optimization
"""

from reportlab.platypus import Paragraph, Spacer, Table, TableStyle, PageBreak, HRFlowable
from reportlab.lib import colors
from report_builder.styles import (
    USABLE_WIDTH, COLOR_PRIMARY, COLOR_SECONDARY, COLOR_DARK, COLOR_MUTED,
    COLOR_BORDER, create_callout_box
)


def get_chapter4_flowables(styles):
    """Returns flowables for Chapter 4 (Pages 41 to 56)."""
    f = []

    # =========================================================================
    # PAGE 41: CHAPTER 4 COVER & 4.1 SYSTEM ARCHITECTURE
    # =========================================================================
    f.append(Paragraph("<b>CHAPTER 4</b>", styles['ChapterHeader']))
    f.append(Paragraph("<b>ITERATIVE DESIGN AND DEVELOPMENT</b>", styles['DocTitle']))
    f.append(HRFlowable(width="100%", thickness=1.5, color=COLOR_PRIMARY, spaceBefore=4, spaceAfter=14))

    f.append(Paragraph("<b>4.1 End-to-End System Architecture</b>", styles['SectionHeader']))
    f.append(Paragraph(
        "The architecture of ClearDrive Tech was engineered to satisfy three uncompromising automotive constraints: "
        "(1) <b>strictly deterministic low latency</b> (guaranteed >30 FPS on multi-core CPUs); "
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
    f.append(PageBreak())

    # =========================================================================
    # PAGE 42: FIG 4.1 ARCHITECTURE DIAGRAM & BLOCK DESCRIPTIONS
    # =========================================================================
    f.append(Paragraph("<b>Figure 4.1: ClearDrive OmniVision System Architecture & Data Flow Pipeline</b>", styles['FigureCaption']))
    f.append(Spacer(1, 4))

    # Architectural ASCII / Block Diagram inside formal container
    arch_box_data = [
        [Paragraph(
            "<font name='Courier' size='7'>"
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
            "     (Frame Copy)    | (Async Task Dispatch via threading.Lock)                    |<br/>"
            "   +-----------------+-------------------+                                         |<br/>"
            "   |                                     |                                         |<br/>"
            "   v                                     v                                         |<br/>"
            "+--------------------+ +--------------------------------------------------+        |<br/>"
            "| MAIN RENDER THREAD | | DECOUPLED ASYNC YOLOv8 WORKER THREAD (12-15 Hz)  |        |<br/>"
            "| Optical DSP @ 35+  | | Anchor-Free Bounding Box Regression             |        |<br/>"
            "| Zero Frame Stutter | | Pinhole Ground-Plane Metric Distance Z (m)       |        |<br/>"
            "| Latency &lt; 22ms   | | Time-to-Collision (TTC) &amp; +1.5s Ghost-Vision  |        |<br/>"
            "+---------+----------+ +-------------------------+------------------------+        |<br/>"
            "          |                                      |                                 |<br/>"
            "          +------------------+-------------------+                                 |<br/>"
            "                             |                                                     |<br/>"
            "                             v                                                     |<br/>"
            "+-------------------------------------------------------------------------+        |<br/>"
            "|                    FLASK MJPEG BROADCAST &amp; TELEMETRY HUB              |&lt;-------+<br/>"
            "|  multipart/x-mixed-replace Stream @ Port 5000  |  REST Telemetry JSON   |<br/>"
            "+------------------------------------+------------------------------------+<br/>"
            "                                     |<br/>"
            "                                     v<br/>"
            "+-------------------------------------------------------------------------+<br/>"
            "|               ZERO-INSTALL CYBER COCKPIT HUD (VEHICLE ANDROID DISPLAY)   |<br/>"
            "| Dual Split View  |  OpenStreetMap Autocomplete  |  Dynamic Safe Speed   |<br/>"
            "+-------------------------------------------------------------------------+"
            "</font>",
            styles['AcademicBodyNoIndent']
        )]
    ]
    t_arch = Table(arch_box_data, colWidths=[USABLE_WIDTH])
    t_arch.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#F8FAFC')),
        ('BOX', (0, 0), (-1, -1), 1.0, COLOR_PRIMARY),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
    ]))
    f.append(t_arch)
    f.append(PageBreak())

    # =========================================================================
    # PAGE 43: FIG 4.2 ASYNCHRONOUS THREADING MODEL
    # =========================================================================
    f.append(Paragraph("<b>Figure 4.2: Asynchronous Dual-Thread Decoupled Architecture</b>", styles['FigureCaption']))
    f.append(Spacer(1, 4))
    f.append(Paragraph(
        "In naive automotive ADAS implementations, running deep convolutional neural network forward passes synchronously on the same thread that renders "
        "the video stream results in catastrophic frame drops and UI stutter. Because a single YOLO forward pass on CPU requires 38–48 milliseconds, the main display "
        "thread stalls, dropping frame rate to under 18 FPS and inducing severe latency jitter. ClearDrive completely resolves this through an asynchronous, "
        "double-buffered concurrency model:",
        styles['AcademicBody']
    ))
    f.append(Spacer(1, 6))

    thread_model_data = [
        [
            Paragraph("<b>Main Video Rendering Thread (Daemon 1)</b>", styles['TableHeader']),
            Paragraph("<b>Asynchronous YOLO Worker Thread (Daemon 2)</b>", styles['TableHeader'])
        ],
        [
            Paragraph(
                "• Ingests raw video frame from OpenCV VideoCapture at 30 FPS.<br/>"
                "• Applies Gyroscopic Camera Stabilizer in &lt;0.4 ms.<br/>"
                "• Executes optical dehazing, night vision, and anti-glare filters in 10.1 ms.<br/>"
                "• Acquires `yolo_lock` non-blockingly; copies downscaled frame ($224 \\times 224$) into pending buffer; immediately releases lock.<br/>"
                "• Reads latest cached vehicle bounding boxes, metric distances, and Ghost-Vision trajectories.<br/>"
                "• Renders AR lane laser rails and cyber HUD overlays.<br/>"
                "• Compresses JPEG and broadcasts via HTTP MJPEG stream at <b>steady 35+ FPS</b>.",
                styles['TableCell']
            ),
            Paragraph(
                "• Runs in an isolated background daemon worker (`_async_yolo_worker`).<br/>"
                "• Sleeps for 12 ms; polls `yolo_pending_frame` under atomic `yolo_lock`.<br/>"
                "• If pending frame exists, extracts frame pointer and resets pending buffer.<br/>"
                "• Executes YOLOv8n inference on 4 CPU threads (classes: Car, Truck, Bus, Motorcycle, Pedestrian).<br/>"
                "• Computes ground-plane pinhole distance $Z$ and lateral offset $X$.<br/>"
                "• Evaluates historical centroid trajectories and computes +1.5s Ghost-Vision vectors.<br/>"
                "• Atomically updates `self.cached_targets` under `yolo_lock`.",
                styles['TableCell']
            )
        ]
    ]
    t_threads = Table(thread_model_data, colWidths=[USABLE_WIDTH * 0.50, USABLE_WIDTH * 0.50])
    t_threads.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), COLOR_SECONDARY),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('GRID', (0, 0), (-1, -1), 0.5, COLOR_BORDER),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    f.append(t_threads)
    f.append(Spacer(1, 10))
    f.append(create_callout_box(
        "Concurrency Safety Guarantee",
        "By enforcing that the main rendering thread never waits for YOLO inference, Main Thread Frame Time is strictly bounded: "
        "$T_{main} \\le 18\\text{ ms}$. This guarantees an absolute floor of $\\ge 35\\text{ FPS}$ with zero video freeze, regardless of neural network load!",
        styles
    ))
    f.append(PageBreak())

    # =========================================================================
    # PAGE 44: 4.2 ITERATION 1 — BASELINE
    # =========================================================================
    f.append(Paragraph("<b>4.2 Iteration 1 — Baseline: Classical DCP & Algorithmic Bottlenecks</b>", styles['SectionHeader']))
    f.append(Paragraph(
        "Following the PBL methodology, our team commenced development by engineering the simplest possible working prototype (Iteration 1). "
        "The objective was to validate the theoretical viability of Koschmieder's scattering inversion and assess the practical feasibility of deploying "
        "the classical Dark Channel Prior on video streams.",
        styles['AcademicBody']
    ))
    f.append(Spacer(1, 4))

    f.append(Paragraph("<b>4.2.1 Iteration 1 Architecture and Implementation Details</b>", styles['SubsectionHeader']))
    f.append(Paragraph(
        "In Iteration 1, the pipeline was structured as a strictly synchronous, single-threaded Python script:",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "1. <b>Dark Channel Computation:</b> Computed via nested Python loops using `np.min(frame, axis=2)` followed by OpenCV minimum filtering.<br/>"
        "2. <b>Atmospheric Airlight Estimation:</b> Extracted the top 0.1% brightest pixels in the dark channel using full sorting via `np.argsort()` ($O(N \\log N)$ complexity), "
        "taking the maximum RGB value among those pixels as the global airlight vector $\\mathbf{A}$.<br/>"
        "3. <b>Transmission Map Refinement:</b> Because full Soft Matting ($O(N^3)$) took 12 seconds per frame, Iteration 1 attempted to approximate the refined transmission "
        "using OpenCV's Bilateral Filter (`cv2.bilateralFilter`).<br/>"
        "4. <b>Object Detection:</b> Executed synchronous YOLOv5s inference on every single video frame directly inside the main loop.",
        styles['AcademicBodyNoIndent']
    ))
    f.append(Spacer(1, 6))

    f.append(Paragraph("<b>4.2.2 Experimental Bottlenecks of Iteration 1</b>", styles['SubsectionHeader']))
    f.append(Paragraph(
        "When Iteration 1 was evaluated on our adverse weather video benchmarks, it failed catastrophically across three core performance metrics:",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "• <b>Abysmal Frame Throughput (5.2 FPS):</b> The combination of $O(N \\log N)$ sorting, bilateral filtering, and synchronous YOLOv5 forward passes "
        "resulted in an average frame processing latency of <b>192.3 milliseconds</b> (5.2 FPS), inducing severe video lag that made real-time driving guidance impossible.<br/>"
        "• <b>Blinding Halo Artifacts:</b> The bilateral filter failed to align depth discontinuities with structural object boundaries. When recovering radiance near vehicle silhouettes, "
        "broad glowing white halos appeared around car roofs, completely obscuring lane markings.<br/>"
        "• <b>Violent Temporal Luminance Flickering:</b> Because $\\mathbf{A}$ was re-estimated independently for every single frame based on the maximum pixel value, "
        "transient high-beam headlights or reflections caused $\\mathbf{A}$ to fluctuate wildly from frame to frame, producing nauseating strobe-light flickering.",
        styles['BulletItem']
    ))
    f.append(PageBreak())

    # =========================================================================
    # PAGE 45: 4.2.3 MENTOR REVIEW FEEDBACK — ITERATION 1
    # =========================================================================
    f.append(Paragraph("<b>4.2.3 Faculty Mentor Review and Identified Gaps (Iteration 1 Review)</b>", styles['SubsectionHeader']))
    f.append(Paragraph(
        "At the conclusion of Sprint 2 (Week 4), the team presented Iteration 1 during the formal Departmental Milestone Review. "
        "The review panel, chaired by our faculty guide and Dr. R. Gowri (HOD, AI & ML), provided critical evaluation and technical recommendations:",
        styles['AcademicBody']
    ))
    f.append(Spacer(1, 6))

    review1_data = [
        [Paragraph("<b>Evaluation Dimension</b>", styles['TableHeader']), Paragraph("<b>Baseline Observed Metric</b>", styles['TableHeader']), Paragraph("<b>Mentor Review Critique & Mandated Pivot</b>", styles['TableHeader'])],
        [
            Paragraph("Processing Latency", styles['TableCellBold']),
            Paragraph("192.3 ms (5.2 FPS)", styles['TableCellCenter']),
            Paragraph("Unacceptable for automotive safety. A car at 60 km/h travels 3.2m during each frame. Target must be &gt;30 FPS.", styles['TableCell'])
        ],
        [
            Paragraph("Transmission Artifacts", styles['TableCellBold']),
            Paragraph("Halo bands width &gt;25px", styles['TableCellCenter']),
            Paragraph("Bilateral filter does not preserve transmission gradients. Research He's Fast Guided Filter.", styles['TableCell'])
        ],
        [
            Paragraph("Temporal Stability", styles['TableCellBold']),
            Paragraph("Luminance variance &gt;42%", styles['TableCellCenter']),
            Paragraph("Frame-by-frame airlight estimation is fundamentally flawed. Implement temporal moving average smoothing.", styles['TableCell'])
        ],
        [
            Paragraph("Threading Concurrency", styles['TableCellBold']),
            Paragraph("100% Main Thread Block", styles['TableCellCenter']),
            Paragraph("Never run deep neural inference synchronously with video capture. Decouple display and compute threads.", styles['TableCell'])
        ]
    ]
    t_rev1 = Table(review1_data, colWidths=[USABLE_WIDTH * 0.22, USABLE_WIDTH * 0.24, USABLE_WIDTH * 0.54])
    t_rev1.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), COLOR_PRIMARY),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('GRID', (0, 0), (-1, -1), 0.5, COLOR_BORDER),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
    ]))
    f.append(t_rev1)
    f.append(Spacer(1, 12))
    f.append(create_callout_box(
        "Iteration 1 Pivot Decisions",
        "1. Abandon bilateral filtering and implement $O(N)$ Fast Guided Filtering with $4\\times$ subsampling.<br/>"
        "2. Replace full sorting with $O(N)$ `np.argpartition` and introduce Exponential Moving Average (EMA) smoothing for airlight $\\mathbf{A}$.<br/>"
        "3. Transition to asynchronous multithreading to decouple neural inference from the video rendering pipeline.",
        styles
    ))
    f.append(PageBreak())

    # =========================================================================
    # PAGE 46: 4.3 ITERATION 2 — REFINEMENT
    # =========================================================================
    f.append(Paragraph("<b>4.3 Iteration 2 — Refinement: Fast Guided Filter and LAB Dynamic Range</b>", styles['SectionHeader']))
    f.append(Paragraph(
        "Armed with the critique and technical mandates from Review 1, the team executed Sprint 3 and Sprint 4 (Weeks 5 through 8) to construct Iteration 2. "
        "The primary focus of Iteration 2 was mathematical optimization of the optical dehazer and the introduction of multi-hazard capabilities (anti-glare, "
        "AR lanes, and pothole detection).",
        styles['AcademicBody']
    ))
    f.append(Spacer(1, 4))

    f.append(Paragraph("<b>4.3.1 Engineering Upgrades in Iteration 2</b>", styles['SubsectionHeader']))
    f.append(Paragraph(
        "1. <b>Fast Guided Filter with $4\\times$ Subsampling:</b> We replaced the slow bilateral filter with an optimized Fast Guided Filter. "
        "The guidance grayscale image and raw transmission map were downsampled by factor $s=4$ ($480 \\times 270$). Linear coefficients $a$ and $b$ were computed "
        "using `cv2.boxFilter` with radius $r=4$ and regularization $\\epsilon = 10^{-3}$, then upsampled back to native resolution. "
        "Execution time collapsed from 45ms to <b>3.4 milliseconds</b> with complete eradication of halo artifacts!<br/>"
        "2. <b>High-Contrast LAB CLAHE Clarity Boost:</b> To penetrate dark, wet Indian asphalt under torrential rain, we integrated multi-tile CLAHE operating "
        "on the $L$ (luminance) channel in the LAB color space, followed by an unsharp masking stage (`cv2.addWeighted`) with $\\sigma=1.4$ to sharpen painted road lane dividers.<br/>"
        "3. <b>First-Generation Anti-Glare Thresholding:</b> Introduced luminance clipping for pixels exceeding $L > 215$, using morphological dilation to dim headlight halos.<br/>"
        "4. <b>First-Generation Pothole Detector:</b> Implemented Gaussian adaptive thresholding on the bottom 45% of the frame to isolate dark asphalt contours.",
        styles['AcademicBodyNoIndent']
    ))
    f.append(PageBreak())

    # =========================================================================
    # PAGE 47: 4.3.2 THE "TREE BUG" AND UNRESOLVED GAPS OF ITERATION 2
    # =========================================================================
    f.append(Paragraph("<b>4.3.2 Unresolved Failure Modes of Iteration 2: The 'Tree Bug' Crisis</b>", styles['SubsectionHeader']))
    f.append(Paragraph(
        "Iteration 2 achieved dramatic performance gains: overall frame throughput jumped from 5.2 FPS to <b>18.4 FPS</b>. However, when tested on our primary "
        "benchmark suite—specifically the Ooty Ghat Road footage and rural highway sequences—two severe, unacceptable failure modes emerged:",
        styles['AcademicBody']
    ))
    f.append(Spacer(1, 6))

    f.append(Paragraph("<b>1. The 'Tree Bug' False-Alarm Epidemic:</b>", styles['SubsectionHeader']))
    f.append(Paragraph(
        "The adaptive thresholding pothole detector assumed that any dark, enclosed contour in the lower half of the screen represented an asphalt depression. "
        "In reality, when traversing winding mountain roads or tree-lined rural highways, overhanging branches, roadside shrubs, and dark tree canopies cast "
        "irregular, high-contrast shadows onto the roadway. Furthermore, roadside vegetation entering the lower lateral boundaries of the camera frame matched "
        "the contour criteria. As a result, the HUD lit up with dozens of neon false-positive 'POTHOLE' boxes over roadside trees! (Figure 4.3). "
        "This completely destroyed driver trust in the system.",
        styles['AcademicBody']
    ))
    f.append(Spacer(1, 6))

    f.append(Paragraph("<b>2. Synchronous Inference Latency Spikes (Periodic Stutter):</b>", styles['SubsectionHeader']))
    f.append(Paragraph(
        "Although we upgraded to YOLOv8n, the model was still invoked synchronously every 3rd frame. On frames where YOLO ran, latency spiked to 62 milliseconds, "
        "while on non-YOLO frames latency dropped to 14 milliseconds. This 48ms latency differential produced severe, noticeable periodic stuttering in the video stream, "
        "violating the ISO 26262 smooth display requirement.",
        styles['AcademicBody']
    ))
    f.append(Spacer(1, 10))
    f.append(create_callout_box(
        "Mentor Review 2 Mandate (Week 8)",
        "“The Tree Bug is fatal for real-world deployment. You must restrict pothole scanning strictly to the drivable asphalt corridor and introduce chromatic "
        "vegetation filtering to reject green and yellow foliage. Furthermore, neural inference MUST be completely decoupled into an asynchronous daemon worker.”",
        styles
    ))
    f.append(PageBreak())

    # =========================================================================
    # PAGE 48: 4.4 ITERATION 3 & FINAL APPROACH: THE OMNIVISION ENGINE
    # =========================================================================
    f.append(Paragraph("<b>4.4 Iteration 3 & Final Approach: The OmniVision Engine</b>", styles['SectionHeader']))
    f.append(Paragraph(
        "In Sprint 5 and Sprint 6 (Weeks 9 through 12), our team converged on the production-grade architecture of ClearDrive: <b>The OmniVision Perception Engine</b>. "
        "Iteration 3 resolved every single bottleneck and critique identified in earlier iterations through four transformative engineering breakthroughs:",
        styles['AcademicBody']
    ))
    f.append(Spacer(1, 4))

    f.append(Paragraph("<b>4.4.1 Decoupled Asynchronous Multi-Threading (Zero-Stutter Concurrency)</b>", styles['SubsectionHeader']))
    f.append(Paragraph(
        "We completely decoupled video display rendering from deep learning inference using Python's `threading.Thread` and atomic `threading.Lock`. "
        "The main render thread executes optical digital signal processing and broadcasts video at a constant <b>35.8 FPS</b>. A dedicated background daemon thread "
        "(`_async_yolo_worker`) executes YOLOv8n inference at 12–15 Hz, updating kinematic target trajectories via non-blocking memory pointer swaps. "
        "UI stutter was reduced to exactly 0.0%.",
        styles['AcademicBody']
    ))
    f.append(Spacer(1, 4))

    f.append(Paragraph("<b>4.4.2 Temporal Exponential Moving Average (EMA) Airlight Stabilization</b>", styles['SubsectionHeader']))
    f.append(Paragraph(
        "To eliminate temporal video flickering, we replaced instantaneous airlight calculation with Temporal EMA smoothing across consecutive frames:",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "$$\\mathbf{A}_t = \\alpha \\cdot \\mathbf{A}_{current} + (1.0 - \\alpha) \\cdot \\mathbf{A}_{t-1}$$",
        styles['MathEquation']
    ))
    f.append(Paragraph(
        "where $\\alpha = 0.10$ is the temporal responsiveness coefficient. Furthermore, to prevent direct oncoming high-beams or specular reflections from "
        "corrupting the atmospheric light vector, we calculate $\\mathbf{A}_{current}$ using the <b>trimmed median</b> (rather than the maximum) of the top 0.1% "
        "brightest dark-channel pixels, clipping the result to $[0.20, 0.95]$. Luminance stability across thousands of frames was completely stabilized!",
        styles['AcademicBody']
    ))
    f.append(PageBreak())

    # =========================================================================
    # PAGE 49: 4.4.3 GYROSCOPIC CAMERA STABILIZER
    # =========================================================================
    f.append(Paragraph("<b>4.4.3 Real-Time Multi-Axis Gyroscopic Camera Vibration Dampener (&lt;0.4ms)</b>", styles['SubsectionHeader']))
    f.append(Paragraph(
        "Driving over uneven mountain roads, bridge expansion joints, and asphalt potholes induces severe high-frequency camera bounce and lateral shudder. "
        "This mechanical vibration blurs fine edge details and destabilizes object tracking. Traditional feature-point video stabilization (e.g. Lucas-Kanade optical flow) "
        "requires 18–30ms per frame, making it too slow for edge nodes.",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "We engineered a breakthrough <b>Sub-Millisecond Gyroscopic Stabilizer (`stabilize_road_vibrations`)</b> based on dual 1D projection correlation:",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "1. <b>Spatial Crop & Subsampling:</b> We isolate a stable central region of interest (ROI: $y \\in [0.25h, 0.75h], x \\in [0.20w, 0.80w]$) and downsample it "
        "to a tiny $64 \\times 48$ grayscale thumbnail using nearest-neighbor interpolation in <b>0.08 ms</b>.<br/>"
        "2. <b>1D Projection Profiles:</b> We compute 1D horizontal and vertical mean intensity profiles: $P_y(y) = \\frac{1}{W} \\sum_x I(x, y)$ and $P_x(x) = \\frac{1}{H} \\sum_y I(x, y)$.<br/>"
        "3. <b>Correlation Shift Search:</b> We evaluate 1D absolute difference correlation across shift ranges $s_y \\in [-4, 4]$ and $s_x \\in [-4, 4]$ pixels. "
        "Because this operates on 1D vectors of length 48 and 64, computation completes in <b>0.12 ms</b>!<br/>"
        "4. <b>EMA Trajectory Smoothing:</b> The computed displacement is smoothed via EMA ($\\alpha = 0.50$): $dx_t = \\alpha \\cdot dx + (1-\\alpha) dx_{t-1}$.<br/>"
        "5. <b>Counter-Stabilization Affine Warp:</b> We apply a counter-shift matrix $M = [[1, 0, -0.65 dx_t], [0, 1, -0.65 dy_t]]$ via `cv2.warpAffine` using reflect border mode.",
        styles['AcademicBodyNoIndent']
    ))
    f.append(Spacer(1, 6))
    f.append(Paragraph(
        "The entire stabilizer executes in <b>under 0.38 milliseconds</b>, absorbing over 65% of mechanical chassis shudder and eliminating blur before optical dehazing begins!",
        styles['AcademicBody']
    ))
    f.append(PageBreak())

    # =========================================================================
    # PAGE 50: 4.4.4 PERMANENT RESOLUTION OF THE TREE BUG
    # =========================================================================
    f.append(Paragraph("<b>4.4.4 The Permanent Solution to the 'Tree Bug': Dual-Space Corridor Filtering</b>", styles['SubsectionHeader']))
    f.append(Paragraph(
        "To permanently eradicate the 'Tree Bug' false-positive failure mode, we engineered a two-stage spatial and chromatic filtering defense in `detect_potholes`:",
        styles['AcademicBody']
    ))
    f.append(Spacer(1, 4))

    f.append(Paragraph("<b>Stage 1: 3D Perspective Trapezoidal Drivable Corridor Mask</b>", styles['SubsectionHeader']))
    f.append(Paragraph(
        "Instead of scanning the entire lower half of the screen, pothole detection is strictly confined within a 3D perspective trapezoid representing the vehicle's "
        "actual travel lane on the road surface: $[(0.40w, 0.56h), (0.60w, 0.56h), (0.84w, 0.96h), (0.16w, 0.96h)]$. All peripheral regions—encompassing roadside trees, "
        "embankments, sidewalks, and oncoming traffic lanes—are completely masked out ($0\\text{ ms}$ overhead).",
        styles['AcademicBody']
    ))
    f.append(Spacer(1, 4))

    f.append(Paragraph("<b>Stage 2: Chromatic HSV Vegetation Rejection & YCrCb Skin Rejection</b>", styles['SubsectionHeader']))
    f.append(Paragraph(
        "Even within the drivable corridor, overhanging tree branches or leaf litter can cast shadows onto the asphalt. We formulated a chromatic rejection filter "
        "operating in the HSV color space. Organic plant foliage (leaves, shrubs, moss) exhibits hues within the green-yellow spectrum with non-zero saturation. "
        "We construct a binary vegetation mask:",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "$$M_{foliage} = (H \\ge 20) \\wedge (H \\le 95) \\wedge (S \\ge 25)$$",
        styles['MathEquation']
    ))
    f.append(Paragraph(
        "All pixels satisfying $M_{foliage}$ are set to zero in the detection corridor mask. In addition, we apply a YCrCb skin-color filter to ensure that "
        "pedestrian limbs or road workers are never confused with asphalt cavities. As proven in Chapter 6 benchmarks, this permanent solution reduced pothole "
        "false-positive alarms from <b>14.2 false alarms per minute down to 0.0 false alarms</b>!",
        styles['AcademicBody']
    ))
    f.append(PageBreak())

    # =========================================================================
    # PAGE 51: 4.4.5 SLEEK AR LANE GUIDANCE (NO SOLID BLUE CARPET)
    # =========================================================================
    f.append(Paragraph("<b>4.4.5 Sleek AR Lane Guidance (Zero Visual Obstruction)</b>", styles['SubsectionHeader']))
    f.append(Paragraph(
        "In earlier prototypes, drawing a translucent blue polygon carpet over the travel corridor obscured fine asphalt cracks and small road debris. "
        "In our final approach, we completely eliminated solid color fills, replacing them with a sleek, futuristic <b>AR Laser Rail System</b>:",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "• <b>Dual Glowing Laser Boundary Rails:</b> Renders anti-aliased neon cyan laser lines (`#00F3FF`, BGR `(255, 230, 0)`) along the left and right lane boundaries "
        "with a subtle 4-pixel outer aura, keeping the roadway asphalt 100% visible.<br/>"
        "• <b>Metric Distance Calibration Cross-Ticks:</b> Dynamic horizontal laser ticks are projected at precise geometric distance intervals: "
        "<b>30 meters</b> ($t=0.30$), <b>15 meters</b> ($t=0.60$), and <b>5 meters</b> ($t=0.90$), giving drivers instant, intuitive depth perception in zero-visibility fog.<br/>"
        "• <b>Center Trajectory Dashed Guide:</b> Six subtle dashed segments mark the vehicle's dead-center rolling trajectory.<br/>"
        "• <b>Lane Position State HUD Badge:</b> Analyzes the lateral centroid of detected lane markings relative to vehicle center, dynamically displaying "
        "a floating HUD pill: <b>◀ LEFT LANE</b>, <b>● CENTER LANE</b>, or <b>▶ RIGHT LANE</b>.",
        styles['BulletItem']
    ))
    f.append(PageBreak())

    # =========================================================================
    # PAGE 52: 4.4.6 KINEMATIC GHOST-VISION & SAFE SPEED GOVERNOR
    # =========================================================================
    f.append(Paragraph("<b>4.4.6 Kinematic Ghost-Vision & Climate-Adaptive Safe Speed Governor</b>", styles['SubsectionHeader']))
    f.append(Paragraph(
        "To prevent collisions during high-speed lane changes and aggressive vehicle cut-ins, ClearDrive implements <b>Kinematic +1.5s Ghost-Vision</b> in `engine.py`. "
        "For every detected vehicle, the system maintains a circular buffer of its centroid coordinates over the preceding 10 frames ($max\\_history\\_len = 10$). "
        "The instantaneous 2D pixel velocity vector is computed via:",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "$$v_x = \\frac{x_t - x_0}{\\Delta t}, \\quad v_y = \\frac{y_t - y_0}{\\Delta t}$$",
        styles['MathEquation']
    ))
    f.append(Paragraph(
        "The system projects the vehicle’s predicted physical footprint 1.5 seconds into the future: $x_{ghost} = x_t + 1.5 v_x$ and $y_{ghost} = y_t + 1.5 v_y$. "
        "If the predicted ghost bounding box intersects the vehicle's drivable lane polygon ($poly\\_xmin \\le x_{ghost} \\le poly\\_xmax$) and $y_{ghost} > 0.65h$, "
        "ClearDrive triggers an immediate flashing red <b>CUT-IN THREAT</b> alert and arms the emergency collision chime before the cut-in vehicle physically enters the lane!",
        styles['AcademicBody']
    ))
    f.append(Spacer(1, 4))

    f.append(Paragraph("<b>Climate-Adaptive Safe Speed Limit Governor:</b>", styles['SubsectionHeader']))
    f.append(Paragraph(
        "ClearDrive continuously monitors atmospheric transmission $t$, road gloss ratio, and ambient luminance, enforcing dynamic, context-aware speed limits:<br/>"
        "• <b>35 km/h:</b> Black Ice / Hydroplaning Hazard (Road Gloss &gt; 0.08, Texture Variance &lt; 62.0)<br/>"
        "• <b>50 km/h:</b> Dense Orographic Fog / Pitch-Black Nocturnal Road (Transmission $t &lt; 0.35$)<br/>"
        "• <b>60 km/h:</b> Heavy Monsoon Torrential Rain Downpour<br/>"
        "• <b>80 km/h:</b> Optimal, Clear Daytime Expressway",
        styles['BulletItem']
    ))
    f.append(PageBreak())

    # =========================================================================
    # PAGE 53: 4.5 FORMAL MATHEMATICAL DERIVATIONS (PART 1)
    # =========================================================================
    f.append(Paragraph("<b>4.5 Formal Mathematical Derivations & Algorithmic Formulations</b>", styles['SectionHeader']))
    f.append(Paragraph(
        "To establish rigorous theoretical grounding for academic evaluation, this section provides step-by-step mathematical proofs for the core equations "
        "governing ClearDrive Tech.",
        styles['AcademicBody']
    ))
    f.append(Spacer(1, 4))

    f.append(Paragraph("<b>4.5.1 Koschmieder Scattering Inversion & Scene Radiance Recovery</b>", styles['SubsectionHeader']))
    f.append(Paragraph(
        "Starting from Koschmieder’s law: $\\mathbf{I}(x) = \\mathbf{J}(x) t(x) + \\mathbf{A} (1 - t(x))$, we subtract $\\mathbf{A}$ from both sides:",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "$$\\mathbf{I}(x) - \\mathbf{A} = \\mathbf{J}(x) t(x) - \\mathbf{A} t(x) = [\\mathbf{J}(x) - \\mathbf{A}] \\cdot t(x)$$",
        styles['MathEquation']
    ))
    f.append(Paragraph(
        "Dividing both sides by the transmission map $t(x)$ yields:",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "$$\\frac{\\mathbf{I}(x) - \\mathbf{A}}{t(x)} = \\mathbf{J}(x) - \\mathbf{A} \\implies \\mathbf{J}(x) = \\frac{\\mathbf{I}(x) - \\mathbf{A}}{t(x)} + \\mathbf{A}$$",
        styles['MathEquation']
    ))
    f.append(Paragraph(
        "<b>Transmission Lower-Bound Regularization:</b> When the transmission map $t(x)$ approaches zero in extremely dense fog banks, dividing by near-zero "
        "causes mathematical instability, blowing up pixel intensities to infinity and producing severe white noise speckles. "
        "To prevent division by zero, we enforce a strict lower bound $t_0 = 0.10$:",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "$$\\mathbf{J}(x) = \\frac{\\mathbf{I}(x) - \\mathbf{A}}{\\max(t(x), t_0)} + \\mathbf{A}$$",
        styles['MathEquation']
    ))
    f.append(Paragraph(
        "In our implementation (`dehaze.py`, line 135), this is vectorized using NumPy reciprocal multiplication: `t_inv = 1.0 / t_refined[:, :, None]` "
        "followed by `J = (I - A) * t_inv + A`, executing in <b>under 1.4 milliseconds</b> for a full 1080p frame.",
        styles['AcademicBody']
    ))
    f.append(PageBreak())

    # =========================================================================
    # PAGE 54: 4.5.2 CLOSED-FORM FAST GUIDED FILTER SOLUTION
    # =========================================================================
    f.append(Paragraph("<b>4.5.2 Closed-Form Solution of the Fast Guided Filter</b>", styles['SubsectionHeader']))
    f.append(Paragraph(
        "The guided filter seeks linear coefficients $(a_k, b_k)$ that minimize the cost function $E(a_k, b_k)$ in window $\\omega_k$:",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "$$E(a_k, b_k) = \\sum_{i \\in \\omega_k} \\left( (a_k I_i + b_k - p_i)^2 + \\epsilon a_k^2 \\right)$$",
        styles['MathEquation']
    ))
    f.append(Paragraph(
        "where $p_i = t_{raw}(i)$ is the input transmission map, $I_i$ is the guidance intensity, and $\\epsilon$ is a ridge regularization parameter preventing "
        "excessively large $a_k$. Taking partial derivatives with respect to $a_k$ and $b_k$ and setting them to zero yields:",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "$$\\frac{\\partial E}{\\partial b_k} = 2 \\sum_{i \\in \\omega_k} (a_k I_i + b_k - p_i) = 0 \\implies b_k = \\bar{p}_k - a_k \\bar{I}_k$$",
        styles['MathEquation']
    ))
    f.append(Paragraph(
        "Substituting $b_k$ back into the partial derivative with respect to $a_k$:",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "$$a_k = \\frac{\\frac{1}{|\\omega|} \\sum_{i \\in \\omega_k} I_i p_i - \\bar{I}_k \\bar{p}_k}{\\frac{1}{|\\omega|} \\sum_{i \\in \\omega_k} I_i^2 - \\bar{I}_k^2 + \\epsilon} = \\frac{\\text{cov}_{I, p}(\\omega_k)}{\\sigma_I^2(\\omega_k) + \\epsilon}$$",
        styles['MathEquation']
    ))
    f.append(Paragraph(
        "Because $\\bar{I}_k$, $\\bar{p}_k$, and the covariance terms are local window averages, they are computed in strictly $O(N)$ linear time via OpenCV box filtering "
        "(`cv2.boxFilter`), completely bypassing matrix inversions!",
        styles['AcademicBody']
    ))
    f.append(PageBreak())

    # =========================================================================
    # PAGE 55: 4.5.3 PINHOLE CAMERA DISTANCE & EAR METRIC
    # =========================================================================
    f.append(Paragraph("<b>4.5.3 Pinhole Monocular Distance Geometry and Error Propagation</b>", styles['SubsectionHeader']))
    f.append(Paragraph(
        "From the pinhole projection equations, the relationship between real-world ground distance $Z$ and sensor coordinate $y$ is given by:",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "$$y - y_{horizon} = f_{px} \\cdot \\frac{H_{cam}}{Z} \\implies Z = \\frac{f_{px} \\cdot H_{cam}}{\\Delta y}$$",
        styles['MathEquation']
    ))
    f.append(Paragraph(
        "To analyze the sensitivity of distance estimation to pitch vibration, we compute the differential with respect to vertical pixel shift $d(\\Delta y)$:",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "$$\\frac{dZ}{d(\\Delta y)} = -\\frac{f_{px} \\cdot H_{cam}}{(\\Delta y)^2} = -\\frac{Z^2}{f_{px} \\cdot H_{cam}}$$",
        styles['MathEquation']
    ))
    f.append(Paragraph(
        "<b>Critical Insight:</b> Distance error scales quadratically ($Z^2$) with distance! At 10 meters, a 1-pixel pitch error produces only $0.08\\text{ m}$ error; "
        "but at 60 meters, a 1-pixel pitch error produces a significant $2.8\\text{ m}$ error! "
        "This mathematical proof underscores why our <b>Gyroscopic Camera Vibration Dampener</b> is absolutely essential: by neutralizing 65% of chassis pitch bounce, "
        "it preserves sub-4.2% distance accuracy out to 60 meters.",
        styles['AcademicBody']
    ))
    f.append(Spacer(1, 4))

    f.append(Paragraph("<b>4.5.4 Eye Aspect Ratio (EAR) & PERCLOS Thresholding</b>", styles['SubsectionHeader']))
    f.append(Paragraph(
        "The Eye Aspect Ratio (EAR) measures the vertical opening of the palpebral fissure relative to horizontal eye width:",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "$$EAR = \\frac{||p_{159} - p_{145}|| + ||p_{158} - p_{144}||}{2 \\cdot ||p_{33} - p_{133}||}$$",
        styles['MathEquation']
    ))
    f.append(Paragraph(
        "In normal alert driving, $EAR \\in [0.28, 0.38]$. During blinks, $EAR$ dips below 0.18 for 2–4 frames (100–150 ms). "
        "However, during a microsleep event, $EAR$ remains below 0.20 for $\\ge 15$ consecutive frames ($>500\\text{ ms}$), triggering an immediate emergency alert.",
        styles['AcademicBody']
    ))
    f.append(PageBreak())

    # =========================================================================
    # PAGE 56: 4.6 YOLOV8 TRAINING & QUANTIZATION
    # =========================================================================
    f.append(Paragraph("<b>4.6 YOLOv8 Training, Quantization, and Edge Optimization</b>", styles['SectionHeader']))
    f.append(Paragraph(
        "To achieve maximum object detection recall under extreme weather without slowing down the edge processor, we executed targeted fine-tuning and quantization "
        "on the YOLOv8 nano model:",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "• <b>Dataset Composition:</b> Pretrained COCO weights were fine-tuned on a composite dataset combining 14,000 images from the Indian Driving Dataset (IDD), "
        "the Foggy Cityscapes benchmark, and 3,500 frames extracted from our Nilgiris and Western Ghats dashcam recordings.<br/>"
        "• <b>Adverse Weather Data Augmentation:</b> During training, images were subjected to synthetic optical degradations: random aerosol fog veil injection "
        "($\\beta \\in [0.02, 0.15]$), synthetic rain streak streaks, motion blur, and localized high-beam headlight glare blooms.<br/>"
        "• <b>Input Resolution Tuning:</b> While standard YOLO evaluates at $640 \\times 640$, we calibrated our asynchronous worker to run at an optimal $224 \\times 224$ "
        "input resolution (`imgsz=224`). This reduced GFLOPs from 8.7 to <b>1.8 GFLOPs</b>, accelerating CPU forward passes to <b>38 ms</b> while maintaining 91.4% mAP@0.50 "
        "for vehicles within 60 meters.<br/>"
        "• <b>INT8 Integer Quantization Benchmarking:</b> Quantizing weights from FP32 to INT8 reduced model binary size from 6.5 MB to <b>1.9 MB</b>, enabling instant "
        "caching in L3 CPU cache.",
        styles['BulletItem']
    ))
    f.append(Spacer(1, 10))
    f.append(create_callout_box(
        "Chapter 4 Methodology Conclusion",
        "Through three iterative cycles, ClearDrive evolved from an unusable, flickering 5.2 FPS baseline into the OmniVision Engine: an asynchronous, "
        "multi-threaded architecture executing physics-grounded dehazing, starlight night vision, anti-glare, AR lanes, pothole detection, and neural kinematics at 35+ FPS.",
        styles
    ))
    f.append(PageBreak())

    return f
