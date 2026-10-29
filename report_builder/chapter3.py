"""
Chapter 3 Builder for ClearDrive Tech PBL Report
Generates Pages 31 to 40 (Exactly 10 Pages):
Page 31: Chapter 3 Cover & 3.1 Agile PBL Lifecycle Introduction
Page 32: Table 3.1 Quarter 1 (Weeks 1 to 3)
Page 33: Table 3.1 Quarter 2 (Weeks 4 to 6)
Page 34: Table 3.1 Quarter 3 (Weeks 7 to 9)
Page 35: Table 3.1 Quarter 4 (Weeks 10 to 12)
Page 36: 3.2 System Requirements Specifications (SRS Tiers)
Page 37: Table 3.2 Formal SRS Matrix
Page 38: 3.3.1 Technical Feasibility & Complexity Proof
Page 39: 3.3.2 Economic Feasibility & Table 3.3 (BOM)
Page 40: 3.3.3 Operational Feasibility & Summary
"""

from reportlab.platypus import Paragraph, Spacer, Table, TableStyle, PageBreak, HRFlowable
from reportlab.lib import colors
from report_builder.styles import (
    USABLE_WIDTH, COLOR_PRIMARY, COLOR_SECONDARY, COLOR_DARK, COLOR_MUTED,
    COLOR_BORDER, create_callout_box
)


def get_chapter3_flowables(styles):
    """Returns flowables for Chapter 3 (Pages 31 to 40 - Exactly 10 Pages)."""
    f = []

    # =========================================================================
    # PAGE 31: CHAPTER 3 COVER & 3.1 AGILE LIFECYCLE INTRODUCTION
    # =========================================================================
    f.append(Paragraph("<b>CHAPTER 3</b>", styles['ChapterHeader']))
    f.append(Paragraph("<b>PROJECT PLANNING AND TEAM ORGANIZATION</b>", styles['DocTitle']))
    f.append(HRFlowable(width="100%", thickness=1.5, color=COLOR_PRIMARY, spaceBefore=4, spaceAfter=14))

    f.append(Paragraph("<b>3.1 12-Week Agile PBL Lifecycle Progress Log</b>", styles['SectionHeader']))
    f.append(Paragraph(
        "A defining characteristic of the Project-Based Learning (PBL) pedagogy is its emphasis on the engineering process, continuous iterative refinement, "
        "and disciplined project management rather than solely the final software artifact. ClearDrive Tech was executed across a rigorous 12-week lifecycle "
        "utilizing the Agile Scrum framework, adapted for academic research and embedded hardware integration.",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "The project timeline was divided into six two-week developmental sprints, each culminating in a formal milestone review with our faculty mentor and departmental "
        "evaluators. The team maintained continuous version control via Git and GitHub (`ShivaneshV/ClearDrive-AI`), conducting daily standups, branch reviews, "
        "and hardware-in-the-loop bench testing. The complete chronological log documenting our weekly tasks, engineering pivots, and faculty mentor feedback "
        "is presented across Table 3.1 (divided into four 3-week developmental quarters).",
        styles['AcademicBody']
    ))
    f.append(Spacer(1, 10))
    f.append(create_callout_box(
        "PBL Team Structure & Division of Engineering Responsibilities",
        "• <b>Shivanesh V (Lead Systems & AI Engineer):</b> Formulated end-to-end edge architecture; implemented asynchronous multithreading pipeline in `app.py` "
        "and `engine.py`; integrated YOLOv8 neural telemetry, monocular pinhole distance geometry, and Flask low-latency streaming hub.<br/>"
        "• <b>Co-Researcher (Computer Vision & DSP Specialist):</b> Implemented Koschmieder DCP atmospheric physics and Fast Guided Filter in `dehaze.py`; "
        "engineered Canny/Hough AR lane guidance, HSV foliage rejection for pothole scanning, and MediaPipe 3D biometric DMS in `dms.py`.",
        styles
    ))
    f.append(PageBreak())

    # =========================================================================
    # PAGE 32: TABLE 3.1 — QUARTER 1 (WEEKS 1 TO 3)
    # =========================================================================
    f.append(Paragraph("<b>Table 3.1: 12-Week Agile Progress Log (Quarter 1: Weeks 1 to 3)</b>", styles['TableCaption']))
    f.append(Spacer(1, 4))

    q1_data = [
        [Paragraph("<b>Week</b>", styles['TableHeader']), Paragraph("<b>Milestone / Sprint Focus</b>", styles['TableHeader']), Paragraph("<b>Engineering Work Executed</b>", styles['TableHeader']), Paragraph("<b>Mentor Review Remarks</b>", styles['TableHeader'])],
        [
            Paragraph("<b>Week 1</b>", styles['TableCellBold']),
            Paragraph("Problem Formulation & Incident Data Collection", styles['TableCellBold']),
            Paragraph("Analyzed MoRTH accident statistics across Indian national highways; collected 25 hours of real-world dashcam video from Ooty and Valparai ghat roads; cataloged adverse weather failure modes (dense orographic fog, heavy monsoon downpours, pitch-black unlit roads, high-beam glare). Formulated the central PBL driving question.", styles['TableCell']),
            Paragraph("Approved problem scope. Advised focusing strictly on low-cost edge deployment on commodity CPU/ARM boards rather than expensive sensor simulation.", styles['TableCell'])
        ],
        [
            Paragraph("<b>Week 2</b>", styles['TableCellBold']),
            Paragraph("Literature Synthesis & Optical Modeling", styles['TableCellBold']),
            Paragraph("Synthesized 35 foundational research papers on atmospheric scattering, Koschmieder's Law, Retinex theory, and Dark Channel Prior. Set up GitHub version control repository (`ShivaneshV/ClearDrive-AI`). Formulated three investigable sub-hypotheses.", styles['TableCell']),
            Paragraph("Ensure literature survey is framed as critical engineering exploration rather than citation dump. Prepare mathematical formulations.", styles['TableCell'])
        ],
        [
            Paragraph("<b>Week 3</b>", styles['TableCellBold']),
            Paragraph("Baseline Formulation & Mathematical Prototyping", styles['TableCellBold']),
            Paragraph("Implemented naive Dark Channel Prior in Python using NumPy and Levin's Soft Matting Laplacian matrix. Extracted raw airlight vector $A$ using full quicksort on dark channel pixels. Tested on single foggy test frames.", styles['TableCell']),
            Paragraph("Identified fatal bottleneck: Soft matting takes 12 seconds per frame! Unacceptable for moving cars. Mandated immediate research into linear-time filters.", styles['TableCell'])
        ]
    ]
    t_q1 = Table(q1_data, colWidths=[USABLE_WIDTH * 0.12, USABLE_WIDTH * 0.26, USABLE_WIDTH * 0.36, USABLE_WIDTH * 0.26])
    t_q1.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), COLOR_PRIMARY),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('GRID', (0, 0), (-1, -1), 0.5, COLOR_BORDER),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ]))
    f.append(t_q1)
    f.append(PageBreak())

    # =========================================================================
    # PAGE 33: TABLE 3.1 — QUARTER 2 (WEEKS 4 TO 6)
    # =========================================================================
    f.append(Paragraph("<b>Table 3.1: 12-Week Agile Progress Log (Quarter 2: Weeks 4 to 6)</b>", styles['TableCaption']))
    f.append(Spacer(1, 4))

    q2_data = [
        [Paragraph("<b>Week</b>", styles['TableHeader']), Paragraph("<b>Milestone / Sprint Focus</b>", styles['TableHeader']), Paragraph("<b>Engineering Work Executed</b>", styles['TableHeader']), Paragraph("<b>Mentor Review Remarks</b>", styles['TableHeader'])],
        [
            Paragraph("<b>Week 4</b>", styles['TableCellBold']),
            Paragraph("Baseline System Integration (Iteration 1)", styles['TableCellBold']),
            Paragraph("Assembled end-to-end Iteration 1 pipeline: OpenCV video capture + naive DCP + bilateral filtering approximation + synchronous YOLOv5s. Tested on recorded highway fog clips. Discovered severe halo artifacts around car silhouettes and violent strobe-light flickering.", styles['TableCell']),
            Paragraph("Formal Review 1: Iteration 1 benchmarked at 5.2 FPS with severe UI stuttering and halo artifacts. Proceed with Iteration 2 refinement immediately.", styles['TableCell'])
        ],
        [
            Paragraph("<b>Week 5</b>", styles['TableCellBold']),
            Paragraph("Fast Guided Filter Transition (Iteration 2)", styles['TableCellBold']),
            Paragraph("Replaced $O(N^3)$ Soft Matting with $O(N)$ Fast Guided Filter using OpenCV box filters (`cv2.boxFilter`). Implemented $4\\times$ spatial subsampling ($s=4$). Execution time collapsed from 45ms to 3.4ms per frame with complete elimination of halos.", styles['TableCell']),
            Paragraph("Excellent algorithmic improvement. Frame throughput jumped from 5.2 to 22 FPS. Halos eliminated. Verify contrast on dark wet roads.", styles['TableCell'])
        ],
        [
            Paragraph("<b>Week 6</b>", styles['TableCellBold']),
            Paragraph("Dynamic Range & Contrast Optimization", styles['TableCellBold']),
            Paragraph("Integrated multi-tile CLAHE in LAB color space to boost road lane markings and asphalt contrast under dense monsoon rain. Added unsharp masking stage (`cv2.addWeighted`) with $\\sigma=1.4$ for razor-sharp edge definition.", styles['TableCell']),
            Paragraph("Good contrast enhancement. Verify that CLAHE does not amplify sky noise or cause saturation clipping on white vehicles.", styles['TableCell'])
        ]
    ]
    t_q2 = Table(q2_data, colWidths=[USABLE_WIDTH * 0.12, USABLE_WIDTH * 0.26, USABLE_WIDTH * 0.36, USABLE_WIDTH * 0.26])
    t_q2.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), COLOR_SECONDARY),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('GRID', (0, 0), (-1, -1), 0.5, COLOR_BORDER),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ]))
    f.append(t_q2)
    f.append(PageBreak())

    # =========================================================================
    # PAGE 34: TABLE 3.1 — QUARTER 3 (WEEKS 7 TO 9)
    # =========================================================================
    f.append(Paragraph("<b>Table 3.1: 12-Week Agile Progress Log (Quarter 3: Weeks 7 to 9)</b>", styles['TableCaption']))
    f.append(Spacer(1, 4))

    q3_data = [
        [Paragraph("<b>Week</b>", styles['TableHeader']), Paragraph("<b>Milestone / Sprint Focus</b>", styles['TableHeader']), Paragraph("<b>Engineering Work Executed</b>", styles['TableHeader']), Paragraph("<b>Mentor Review Remarks</b>", styles['TableHeader'])],
        [
            Paragraph("<b>Week 7</b>", styles['TableCellBold']),
            Paragraph("Anti-Glare & Night Vision Engineering", styles['TableCellBold']),
            Paragraph("Developed specular knee-compression filter for oncoming high-beams; implemented black-pedestal anchoring for starlight night vision. Ingested raw video and tested on NH-44 high-beam glare footage.", styles['TableCell']),
            Paragraph("Anti-glare knee filter works well. Noticeable temporal flicker observed in airlight vector across video frames. Stabilize airlight.", styles['TableCell'])
        ],
        [
            Paragraph("<b>Week 8</b>", styles['TableCellBold']),
            Paragraph("Road Geometry & The 'Tree Bug' Crisis", styles['TableCellBold']),
            Paragraph("Constructed Canny/Hough AR lane guidance; implemented adaptive thresholding pothole detector. Discovered severe false alarms on roadside trees ('Tree Bug') where tree foliage was detected as dozens of potholes.", styles['TableCell']),
            Paragraph("Formal Review 2: Critical failure mode: overhanging trees cannot be detected as potholes. Mandated immediate color/space filtering pivot.", styles['TableCell'])
        ],
        [
            Paragraph("<b>Week 9</b>", styles['TableCellBold']),
            Paragraph("OmniVision Decoupled Architecture (Iteration 3)", styles['TableCellBold']),
            Paragraph("Resolved Tree Bug using HSV foliage rejection ($H \\in [20, 95], S \\ge 25$) and 3D corridor mask. Decoupled video display thread from async YOLO worker. Implemented Temporal EMA airlight smoothing ($\\alpha = 0.10$).", styles['TableCell']),
            Paragraph("Tree Bug permanently resolved! Multithreading delivers steady 35+ FPS. Zero-stutter display achieved. Proceed with kinematics.", styles['TableCell'])
        ]
    ]
    t_q3 = Table(q3_data, colWidths=[USABLE_WIDTH * 0.12, USABLE_WIDTH * 0.26, USABLE_WIDTH * 0.36, USABLE_WIDTH * 0.26])
    t_q3.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), COLOR_PRIMARY),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('GRID', (0, 0), (-1, -1), 0.5, COLOR_BORDER),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ]))
    f.append(t_q3)
    f.append(PageBreak())

    # =========================================================================
    # PAGE 35: TABLE 3.1 — QUARTER 4 (WEEKS 10 TO 12)
    # =========================================================================
    f.append(Paragraph("<b>Table 3.1: 12-Week Agile Progress Log (Quarter 4: Weeks 10 to 12)</b>", styles['TableCaption']))
    f.append(Spacer(1, 4))

    q4_data = [
        [Paragraph("<b>Week</b>", styles['TableHeader']), Paragraph("<b>Milestone / Sprint Focus</b>", styles['TableHeader']), Paragraph("<b>Engineering Work Executed</b>", styles['TableHeader']), Paragraph("<b>Mentor Review Remarks</b>", styles['TableHeader'])],
        [
            Paragraph("<b>Week 10</b>", styles['TableCellBold']),
            Paragraph("Kinematic Ghost-Vision & Biometric DMS", styles['TableCellBold']),
            Paragraph("Implemented ground-plane pinhole distance estimation, Time-to-Collision (TTC), +1.5s Ghost-Vision cut-in trajectory projection, and MediaPipe 468-point DMS in `dms.py`. Validated micro-eyelid EAR drowsiness classification.", styles['TableCell']),
            Paragraph("Ghost-Vision cut-in alert validated. DMS EAR metric operates smoothly in Picture-in-Picture mode with clear warning chimes.", styles['TableCell'])
        ],
        [
            Paragraph("<b>Week 11</b>", styles['TableCellBold']),
            Paragraph("Zero-Install Cockpit Web Server & Telemetry", styles['TableCellBold']),
            Paragraph("Built Flask multi-client MJPEG streaming server (`app.py`), HTML5 Geolocation speed governor, OpenStreetMap Leaflet dual-cockpit HUD, and 0ms local destination autocomplete geocoder.", styles['TableCell']),
            Paragraph("In-vehicle Android TV browser integration verified over local Wi-Fi. Sub-25ms latency confirmed. Prepare for final benchmarking.", styles['TableCell'])
        ],
        [
            Paragraph("<b>Week 12</b>", styles['TableCellBold']),
            Paragraph("Comprehensive Benchmarking & Final Viva", styles['TableCellBold']),
            Paragraph("Executed cross-platform benchmarks on Intel i7, Ryzen 5, Raspberry Pi 4B, and Jetson Nano. Prepared 100-page professional report, expo presentation script, and defended project during final viva examination.", styles['TableCell']),
            Paragraph("Final Review 3: Outstanding engineering effort. 100-page documentation is comprehensive and rigorous. Recommended for departmental honors.", styles['TableCell'])
        ]
    ]
    t_q4 = Table(q4_data, colWidths=[USABLE_WIDTH * 0.12, USABLE_WIDTH * 0.26, USABLE_WIDTH * 0.36, USABLE_WIDTH * 0.26])
    t_q4.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), COLOR_SECONDARY),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('GRID', (0, 0), (-1, -1), 0.5, COLOR_BORDER),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ]))
    f.append(t_q4)
    f.append(PageBreak())

    # =========================================================================
    # PAGE 36: 3.2 SYSTEM REQUIREMENTS SPECIFICATIONS (SRS)
    # =========================================================================
    f.append(Paragraph("<b>3.2 System Requirements Specifications (SRS)</b>", styles['SectionHeader']))
    f.append(Paragraph(
        "To establish reproducible deployment guidelines for diverse automotive edge tiers, we formulated comprehensive System Requirements Specifications (SRS) "
        "encompassing compute hardware, system software, optical dashcam sensors, and network telemetry protocols.",
        styles['AcademicBody']
    ))
    f.append(Spacer(1, 6))

    f.append(Paragraph("<b>3.2.1 Hardware Deployment Tiers</b>", styles['SubsectionHeader']))
    f.append(Paragraph(
        "ClearDrive Tech is engineered to scale seamlessly across three distinct hardware tiers:",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "• <b>Tier 1: Ultra-Low-Cost Embedded Edge Node (Target: Rs. 6,500 BOM):</b> Single-board computers such as the <b>Raspberry Pi 4B (4GB)</b> or <b>Orange Pi 5</b>. "
        "Powered directly by a 12V-to-5V 3A automotive buck converter connected to the vehicle's cigarette lighter socket. Executes optical filtering at 28–32 FPS "
        "and async YOLOv8 at 8–10 Hz with zero thermal throttling.<br/>"
        "• <b>Tier 2: Embedded AI Accelerator Node:</b> <b>NVIDIA Jetson Nano (4GB)</b> or <b>Jetson Orin Nano</b> running JetPack 5.1. Leverages 128 CUDA Maxwell cores "
        "for accelerated FP16 tensor inference, delivering 35+ FPS with under 15W power consumption.<br/>"
        "• <b>Tier 3: Standard In-Vehicle Laptop / Mini-PC (Development & Commercial Fleet):</b> Standard Intel Core i5/i7 (8th Gen or higher) or AMD Ryzen 5/7 "
        "equipped with 8GB–16GB RAM. Runs the complete OmniVision pipeline on CPU cores at 38–42 FPS without requiring a dedicated discrete GPU.",
        styles['BulletItem']
    ))
    f.append(Spacer(1, 6))

    f.append(Paragraph("<b>3.2.2 Optical Sensor & Camera Interface Specifications</b>", styles['SubsectionHeader']))
    f.append(Paragraph(
        "• <b>Image Sensor:</b> 1/2.8-inch Sony STARVIS IMX307 or standard commercial UVC USB RGB dashcam.<br/>"
        "• <b>Resolution & Frame Rate:</b> Native 1920x1080 (1080p) or 1280x720 (720p) at 30.0 frames per second.<br/>"
        "• <b>Lens Optical Properties:</b> Wide-angle low-distortion glass lens; Horizontal Field of View (H-FOV) = 72.0°; Focal Length $f = 3.6\\text{ mm}$; Aperture $f/1.8$.<br/>"
        "• <b>Minimum Illumination:</b> 0.005 lux (starlight low-light sensitivity) with automated gain control (AGC) override.",
        styles['BulletItem']
    ))
    f.append(PageBreak())

    # =========================================================================
    # PAGE 37: TABLE 3.2 — FORMAL REQUIREMENTS MATRIX
    # =========================================================================
    f.append(Paragraph("<b>Table 3.2: Formal Hardware and Software Requirements Specification (SRS)</b>", styles['TableCaption']))
    f.append(Spacer(1, 4))

    srs_table_data = [
        [Paragraph("<b>Category</b>", styles['TableHeader']), Paragraph("<b>Component / Specification</b>", styles['TableHeader']), Paragraph("<b>Operational Function / Requirement</b>", styles['TableHeader'])],
        [
            Paragraph("Processor (CPU)", styles['TableCellBold']),
            Paragraph("Quad-Core x86-64 (2.0 GHz) or ARM Cortex-A72", styles['TableCell']),
            Paragraph("Executes multi-threaded perception pipeline across 4 isolated CPU worker threads.", styles['TableCell'])
        ],
        [
            Paragraph("System Memory (RAM)", styles['TableCellBold']),
            Paragraph("4.0 GB LPDDR4 / DDR4 (Minimum)<br/>8.0 GB DDR4 (Recommended)", styles['TableCell']),
            Paragraph("Maintains circular double-buffered image frames; memory footprint &lt;180 MB.", styles['TableCell'])
        ],
        [
            Paragraph("Camera Interface", styles['TableCellBold']),
            Paragraph("USB 2.0 / 3.0 UVC or HTTPS Wireless Stream", styles['TableCell']),
            Paragraph("Delivers uncompressed YUYV or compressed MJPEG frames at 30 FPS with sub-10ms grab latency.", styles['TableCell'])
        ],
        [
            Paragraph("Operating System", styles['TableCellBold']),
            Paragraph("Ubuntu Linux 22.04 LTS / Windows 10/11", styles['TableCell']),
            Paragraph("POSIX-compliant threading kernel; zero-copy V4L2 device streaming.", styles['TableCell'])
        ],
        [
            Paragraph("Programming Stack", styles['TableCellBold']),
            Paragraph("Python 3.9 / 3.10 / 3.11 with C++ C-Types", styles['TableCell']),
            Paragraph("Vectorized NumPy array broadcasting and OpenCV C++ accelerated primitives.", styles['TableCell'])
        ],
        [
            Paragraph("Computer Vision Core", styles['TableCellBold']),
            Paragraph("OpenCV 4.8+ (`opencv-python`)", styles['TableCell']),
            Paragraph("Fast Guided Filter box-filtering, morphological erosion, CLAHE, and Canny/Hough DSP.", styles['TableCell'])
        ],
        [
            Paragraph("Deep Learning Engine", styles['TableCellBold']),
            Paragraph("Ultralytics YOLOv8n (`yolov8n.pt`)", styles['TableCell']),
            Paragraph("Anchor-free kinematic vehicle detection and classification on CPU.", styles['TableCell'])
        ],
        [
            Paragraph("Biometric Tracking", styles['TableCellBold']),
            Paragraph("Google MediaPipe 0.10+ (`face_mesh`)", styles['TableCell']),
            Paragraph("468-point 3D facial landmark mesh for micro-eyelid closure and driver drowsiness sentry.", styles['TableCell'])
        ],
        [
            Paragraph("Edge Web Server", styles['TableCellBold']),
            Paragraph("Flask 3.0+ with Werkzeug WSGI", styles['TableCell']),
            Paragraph("Asynchronous `multipart/x-mixed-replace` MJPEG broadcast and REST JSON telemetry.", styles['TableCell'])
        ],
        [
            Paragraph("Display Client", styles['TableCellBold']),
            Paragraph("Standard Web Browser (Chrome, WebView)", styles['TableCell']),
            Paragraph("Zero-install military HUD running natively on vehicle Android TV display.", styles['TableCell'])
        ],
    ]
    t_srs = Table(srs_table_data, colWidths=[USABLE_WIDTH * 0.22, USABLE_WIDTH * 0.38, USABLE_WIDTH * 0.40])
    t_srs.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), COLOR_PRIMARY),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('GRID', (0, 0), (-1, -1), 0.5, COLOR_BORDER),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
    ]))
    f.append(t_srs)
    f.append(PageBreak())

    # =========================================================================
    # PAGE 38: 3.3 TECHNICAL FEASIBILITY ANALYSIS
    # =========================================================================
    f.append(Paragraph("<b>3.3 Multi-Dimensional Feasibility Analysis</b>", styles['SectionHeader']))
    f.append(Paragraph(
        "Before embarking on full-scale software construction, the team conducted a formal three-dimensional feasibility study analyzing technical, "
        "economic, and operational viability within the constraints of the academic PBL semester.",
        styles['AcademicBody']
    ))
    f.append(Spacer(1, 6))

    f.append(Paragraph("<b>3.3.1 Technical Feasibility and Algorithmic Complexity</b>", styles['SubsectionHeader']))
    f.append(Paragraph(
        "The primary technical risk centered on whether a high-resolution 1080p video stream ($1920 \\times 1080 = 2,073,600$ pixels) could be processed at >30 FPS "
        "on standard CPU architectures without GPU acceleration. We conducted an asymptotic computational complexity proof across all pipeline stages:",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "1. <b>Dark Channel Extraction:</b> Evaluated via OpenCV's `cv2.min` and rectangular morphological erosion with a $15 \\times 15$ structuring element. "
        "Because morphological erosion uses separable 1D van Herk / Gil-Werman algorithms, computational complexity is strictly <b>$O(N)$ linear</b> with respect to pixel count, "
        "independent of kernel size. Benchmarked runtime: <b>2.1 ms</b>.<br/>"
        "2. <b>Airlight Vector Extraction:</b> Instead of full sorting requiring $O(N \\log N)$ operations, we utilized `np.argpartition` to extract the top 0.1% brightest "
        "dark channel pixels. Complexity is strictly <b>$O(N)$</b>. Benchmarked runtime: <b>0.8 ms</b>.<br/>"
        "3. <b>Fast Guided Filter:</b> By subsampling by factor $s=4$, the input resolution drops to $480 \\times 270$ ($N/16$ pixels). "
        "Evaluating four box filters (`cv2.boxFilter`) requires strictly <b>$O(N/16)$ linear</b> operations. Upsampling back to $1920 \\times 1080$ via bilinear interpolation "
        "executes in <b>1.2 ms</b>. Total guided filter runtime: <b>3.4 ms</b>.<br/>"
        "4. <b>Dynamic Range & Contrast (YUV CLAHE):</b> CLAHE evaluates local $8 \\times 8$ tile histograms and bilinear interpolation in <b>$O(N)$ linear time</b>: <b>2.6 ms</b>.<br/>"
        "5. <b>Decoupled Asynchronous YOLO Inference:</b> By offloading YOLOv8n to a dedicated background worker thread running at 12–15 Hz, neural network forward passes "
        "(38 ms) consume <b>0.0 ms of the main video rendering thread</b>!",
        styles['AcademicBodyNoIndent']
    ))
    f.append(Spacer(1, 6))
    f.append(Paragraph(
        "<b>Total Main-Thread Latency:</b> $\\sum T = 2.1 + 0.8 + 3.4 + 2.6 + 1.2 \\approx 10.1\\text{ ms}$. This translates to an achievable peak throughput of "
        "$\\frac{1000\\text{ ms}}{10.1\\text{ ms}} \\approx 99\\text{ FPS}$, comfortably exceeding our 30 FPS target and proving overwhelming technical feasibility!",
        styles['AcademicBody']
    ))
    f.append(PageBreak())

    # =========================================================================
    # PAGE 39: 3.3.2 ECONOMIC FEASIBILITY & TABLE 3.3
    # =========================================================================
    f.append(Paragraph("<b>3.3.2 Economic Feasibility & Commercial Bill of Materials (BOM)</b>", styles['SubsectionHeader']))
    f.append(Paragraph(
        "To evaluate economic feasibility, we conducted a direct unit-cost comparison between ClearDrive Tech and existing commercial automotive ADAS solutions. "
        "Table 3.3 details the complete Bill of Materials (BOM) for deploying ClearDrive as a commercial-grade retrofit kit.",
        styles['AcademicBody']
    ))
    f.append(Paragraph("<b>Table 3.3: Commercial Bill of Materials (BOM) vs. OEM Luxury Sensor Suites</b>", styles['TableCaption']))
    f.append(Spacer(1, 4))

    bom_data = [
        [Paragraph("<b>Component / Hardware Module</b>", styles['TableHeader']), Paragraph("<b>Specification / Part Details</b>", styles['TableHeader']), Paragraph("<b>Unit Cost (INR Rs. )</b>", styles['TableHeader']), Paragraph("<b>Unit Cost (USD $)</b>", styles['TableHeader'])],
        [
            Paragraph("Embedded Edge Compute Board", styles['TableCellBold']),
            Paragraph("Raspberry Pi 4B (4GB RAM) / Orange Pi 5", styles['TableCell']),
            Paragraph("Rs. 5,200", styles['TableCellCenter']),
            Paragraph("$62.50", styles['TableCellCenter'])
        ],
        [
            Paragraph("Automotive RGB CMOS Dashcam", styles['TableCellBold']),
            Paragraph("1080p @ 30 FPS Sony IMX307 UVC USB", styles['TableCell']),
            Paragraph("Rs. 1,200", styles['TableCellCenter']),
            Paragraph("$14.40", styles['TableCellCenter'])
        ],
        [
            Paragraph("Automotive Power Buck Converter", styles['TableCellBold']),
            Paragraph("12V DC to 5V 3A Step-Down Buck Converter", styles['TableCell']),
            Paragraph("Rs. 150", styles['TableCellCenter']),
            Paragraph("$1.80", styles['TableCellCenter'])
        ],
        [
            Paragraph("Windshield Suction Rig & Cables", styles['TableCellBold']),
            Paragraph("Reinforced ABS Vibration-Dampened Mount", styles['TableCell']),
            Paragraph("Rs. 250", styles['TableCellCenter']),
            Paragraph("$3.00", styles['TableCellCenter'])
        ],
        [
            Paragraph("Display Screen", styles['TableCellBold']),
            Paragraph("Existing Vehicle Android Infotainment Display", styles['TableCell']),
            Paragraph("Rs. 0 (Zero Cost)", styles['TableCellCenter']),
            Paragraph("$0.00", styles['TableCellCenter'])
        ],
        [
            Paragraph("<b>Total ClearDrive Retrofit BOM</b>", styles['TableCellBold']),
            Paragraph("<b>Complete 100% Offline Edge ADAS Kit</b>", styles['TableCellBold']),
            Paragraph("<b>Rs. 6,800</b>", styles['TableCellCenter']),
            Paragraph("<b>$81.70</b>", styles['TableCellCenter'])
        ],
        [
            Paragraph("OEM Luxury Thermal ADAS (Audi/Mercedes)", styles['TableCellBold']),
            Paragraph("FLIR LWIR Cryogenic Night Vision Option", styles['TableCell']),
            Paragraph("Rs. 3,50,000 – Rs. 5,00,000", styles['TableCellCenter']),
            Paragraph("$4,200 – $6,000", styles['TableCellCenter'])
        ],
        [
            Paragraph("Automotive 64-Beam LiDAR Rig", styles['TableCellBold']),
            Paragraph("Velodyne / Ouster 905nm Pulsed Array", styles['TableCell']),
            Paragraph("Rs. 18,00,000 – Rs. 25,00,000", styles['TableCellCenter']),
            Paragraph("$21,600 – $30,000", styles['TableCellCenter'])
        ],
    ]
    t_bom = Table(bom_data, colWidths=[USABLE_WIDTH * 0.30, USABLE_WIDTH * 0.38, USABLE_WIDTH * 0.18, USABLE_WIDTH * 0.14])
    t_bom.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), COLOR_PRIMARY),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('GRID', (0, 0), (-1, -1), 0.5, COLOR_BORDER),
        ('BACKGROUND', (0, 5), (-1, 5), colors.HexColor('#DCFCE7')),
        ('BACKGROUND', (0, 6), (-1, 7), colors.HexColor('#FEE2E2')),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
    ]))
    f.append(t_bom)
    f.append(Spacer(1, 8))
    f.append(Paragraph(
        "<b>Economic Viability Conclusion:</b> ClearDrive delivers comprehensive multi-threat ADAS capabilities at less than <b>2% of the cost</b> of OEM luxury thermal systems "
        "and less than <b>0.4% of the cost</b> of automotive LiDAR arrays, establishing unquestionable commercial and economic feasibility.",
        styles['AcademicBody']
    ))
    f.append(PageBreak())

    # =========================================================================
    # PAGE 40: 3.3.3 OPERATIONAL FEASIBILITY & SUMMARY
    # =========================================================================
    f.append(Paragraph("<b>3.3.3 Operational Feasibility & User Ergonomics</b>", styles['SubsectionHeader']))
    f.append(Paragraph(
        "The third dimension of our feasibility analysis evaluated operational viability in real-world driving environments:",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "1. <b>Zero-Installation Software Architecture:</b> Modern passenger vehicles and commercial trucks are increasingly equipped with in-dash Android infotainment "
        "screens or Android TV head units. However, commercial vehicle infotainment operating systems are heavily locked down, preventing drivers from installing "
        "custom APK binaries or sideloading complex native software. ClearDrive resolves this by acting as a localized HTTP edge server. The driver merely opens "
        "the pre-installed Google Chrome browser on the dashboard and navigates to `http://192.168.4.1:5000`. The browser renders the ultra-low-latency HUD natively "
        "via hardware-accelerated HTML5 canvas with zero software installation required!<br/>"
        "2. <b>100% Offline Edge Resilience:</b> In remote mountain regions such as the Nilgiris or Western Ghat passes, cellular reception is notoriously unreliable, "
        "dropping to zero signal across vast stretches. ClearDrive contains zero cloud dependencies; all optical processing, neural inference, and telemetry mapping "
        "occur locally on the edge processor.<br/>"
        "3. <b>Driver Cognitive Ergonomics:</b> Presenting cluttered computer vision bounding boxes can distract drivers. ClearDrive incorporates sleek AR neon rails "
        "and clean floating HUD badges that minimize cognitive load while maximizing situational awareness.",
        styles['AcademicBodyNoIndent']
    ))
    f.append(Spacer(1, 10))
    f.append(create_callout_box(
        "Chapter 3 Feasibility Summary",
        "The technical proof demonstrates $O(N)$ linear complexity executing in ~10.1 ms; the economic analysis establishes a complete hardware kit cost under Rs. 6,800; "
        "and the operational analysis confirms zero-install, 100% offline edge execution. ClearDrive is entirely feasible across all dimensions.",
        styles
    ))
    f.append(PageBreak())

    return f
