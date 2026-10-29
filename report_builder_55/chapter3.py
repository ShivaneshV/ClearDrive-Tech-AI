"""
Chapter 3: Project Planning and Team Organization (Pages 18 to 22 — Exactly 5 Pages)
ClearDrive AI: Real-Time ADAS and Vision Restoration for Adverse Driving Conditions
"""

from reportlab.platypus import Paragraph, Spacer, Table, TableStyle, PageBreak, HRFlowable
from reportlab.lib import colors
from report_builder_55.styles import (
    USABLE_WIDTH, COLOR_PRIMARY, COLOR_SECONDARY, COLOR_BORDER,
    create_callout_box
)


def get_chapter3_flowables(styles):
    """Returns flowables for Chapter 3 (Pages 18 to 22 - Exactly 5 Pages)."""
    f = []

    # =========================================================================
    # PAGE 18: CHAPTER 3 COVER, LIFECYCLE & TABLE 3.1 PART 1 (WEEKS 1 TO 6)
    # =========================================================================
    f.append(Paragraph("<b>CHAPTER 3</b>", styles['ChapterHeader']))
    f.append(Paragraph("<b>PROJECT PLANNING AND TEAM ORGANIZATION</b>", styles['DocTitle']))
    f.append(HRFlowable(width="100%", thickness=1.2, color=COLOR_PRIMARY, spaceBefore=2, spaceAfter=8))

    f.append(Paragraph("<b>3.1 12-Week Agile PBL Lifecycle Progress Log</b>", styles['SectionHeader']))
    f.append(Paragraph(
        "A defining characteristic of the Project-Based Learning (PBL) pedagogy is its emphasis on disciplined engineering process, continuous iterative "
        "refinement, and collaborative accountability rather than solely the final software artifact. ClearDrive AI was executed across a rigorous 12-week "
        "lifecycle utilizing the Agile Scrum framework, adapted for academic research and embedded hardware-in-the-loop integration.",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "The project was organized into six two-week developmental sprints, each culminating in a formal milestone review with our faculty mentor and "
        "departmental evaluators. Continuous version control was maintained via Git (`ShivaneshV/ClearDrive-AI`). Table 3.1 documents the chronological log "
        "of tasks, technical pivots, and mentor evaluations across Weeks 1 to 6:",
        styles['AcademicBody']
    ))
    f.append(Spacer(1, 2))
    f.append(Paragraph("<b>Table 3.1: 12-Week Agile PBL Lifecycle Progress Log (Sprints 1 to 3)</b>", styles['TableCaption']))

    log_part1_data = [
        [Paragraph("<b>Wk / Sprint</b>", styles['TableHeader']), Paragraph("<b>Developmental Focus &amp; Objectives</b>", styles['TableHeader']), Paragraph("<b>Key Technical Deliverables &amp; Engineering Decisions</b>", styles['TableHeader']), Paragraph("<b>Status / Sign-off</b>", styles['TableHeader'])],
        [
            Paragraph("<b>W1: Spr 1</b>", styles['TableCellBold']),
            Paragraph("Problem Scoping &amp; Highway Data Analysis", styles['TableCell']),
            Paragraph("Analyzed MoRTH crash datasets; mapped Western Ghats &amp; Yamuna Expressway fog hazard corridors; drafted ODD boundaries.", styles['TableCell']),
            Paragraph("Completed [Mentor Verified]", styles['TableCellCenter'])
        ],
        [
            Paragraph("<b>W2: Spr 1</b>", styles['TableCellBold']),
            Paragraph("Sensor Failure Audit &amp; Literature Synthesis", styles['TableCell']),
            Paragraph("Benchmarked LiDAR/Radar rain/fog deficits; synthesized 35 foundational papers; established monocular vision + edge AI roadmap.", styles['TableCell']),
            Paragraph("Completed [Mentor Verified]", styles['TableCellCenter'])
        ],
        [
            Paragraph("<b>W3: Spr 2</b>", styles['TableCellBold']),
            Paragraph("Atmospheric Physics Modeling &amp; Dark Channel", styles['TableCell']),
            Paragraph("Implemented Koschmieder radiative transfer in Python; formulated patch-based Dark Channel Prior (DCP) with window r=15.", styles['TableCell']),
            Paragraph("Completed [Mentor Verified]", styles['TableCellCenter'])
        ],
        [
            Paragraph("<b>W4: Spr 2</b>", styles['TableCellBold']),
            Paragraph("Iteration 1: Baseline Engine Development", styles['TableCell']),
            Paragraph("Constructed monolithic sequential pipeline; integrated Levin Soft Matting Laplacian for transmission map refinement.", styles['TableCell']),
            Paragraph("Completed [Mentor Verified]", styles['TableCellCenter'])
        ],
        [
            Paragraph("<b>W5: Spr 3</b>", styles['TableCellBold']),
            Paragraph("Profiling &amp; Diagnosis of 1.8 FPS Bottleneck", styles['TableCell']),
            Paragraph("Identified O(N^2) Soft Matting linear solve as fatal choke point (20s/frame, 3.5GB RAM); initiated algorithmic pivot.", styles['TableCell']),
            Paragraph("Completed [Mentor Verified]", styles['TableCellCenter'])
        ],
        [
            Paragraph("<b>W6: Spr 3</b>", styles['TableCellBold']),
            Paragraph("Iteration 2: Fast Guided Filter Implementation", styles['TableCell']),
            Paragraph("Vectorized O(N) Fast Guided Filter with subsampling factor s=4; restored throughput to 45 FPS; eliminated RAM exhaustion.", styles['TableCell']),
            Paragraph("Completed [Mentor Verified]", styles['TableCellCenter'])
        ],
    ]
    t_log1 = Table(log_part1_data, colWidths=[USABLE_WIDTH * 0.15, USABLE_WIDTH * 0.28, USABLE_WIDTH * 0.43, USABLE_WIDTH * 0.14])
    t_log1.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), COLOR_PRIMARY),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('GRID', (0, 0), (-1, -1), 0.5, COLOR_BORDER),
        ('TOPPADDING', (0, 0), (-1, -1), 2.2),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2.2),
    ]))
    f.append(t_log1)
    f.append(PageBreak())

    # =========================================================================
    # PAGE 19: 3.1 CONTINUED — TABLE 3.1 PART 2 (WEEKS 7 TO 12) & RETROSPECTIVE
    # =========================================================================
    f.append(Paragraph("<b>3.1 Continued: Sprint Progress Matrix (Weeks 7 to 12)</b>", styles['SectionHeader']))
    f.append(Paragraph(
        "The second half of the project focused on resolving edge-case visual artifacts, introducing asynchronous multiprocessing concurrency, "
        "and conducting in-vehicle highway validation. Table 3.1 (Part 2) chronicles Weeks 7 to 12:",
        styles['AcademicBody']
    ))
    f.append(Spacer(1, 2))
    f.append(Paragraph("<b>Table 3.1: 12-Week Agile PBL Lifecycle Progress Log (Sprints 4 to 6)</b>", styles['TableCaption']))

    log_part2_data = [
        [Paragraph("<b>Wk / Sprint</b>", styles['TableHeader']), Paragraph("<b>Developmental Focus &amp; Objectives</b>", styles['TableHeader']), Paragraph("<b>Key Technical Deliverables &amp; Engineering Decisions</b>", styles['TableHeader']), Paragraph("<b>Status / Sign-off</b>", styles['TableHeader'])],
        [
            Paragraph("<b>W7: Spr 4</b>", styles['TableCellBold']),
            Paragraph("Discovery &amp; Diagnosis of the 'Tree Bug'", styles['TableCell']),
            Paragraph("Diagnosed dark foliage transmission collapse causing intense white-halo artifacts around tree canopies; analyzed math origin.", styles['TableCell']),
            Paragraph("Completed [Mentor Verified]", styles['TableCellCenter'])
        ],
        [
            Paragraph("<b>W8: Spr 4</b>", styles['TableCellBold']),
            Paragraph("Dynamic Transmission Normalization &amp; EMA", styles['TableCell']),
            Paragraph("Introduced t0=0.15 floor and temporal Exponential Moving Average (alpha=0.05) on airlight A; completely eradicated sky flickering.", styles['TableCell']),
            Paragraph("Completed [Mentor Verified]", styles['TableCellCenter'])
        ],
        [
            Paragraph("<b>W9: Spr 5</b>", styles['TableCellBold']),
            Paragraph("Iteration 3: OmniVision Multi-Threading Engine", styles['TableCell']),
            Paragraph("Architected decoupled Python multiprocessing worker pools; isolated YOLOv8 neural inference from real-time MJPEG streaming thread.", styles['TableCell']),
            Paragraph("Completed [Mentor Verified]", styles['TableCellCenter'])
        ],
        [
            Paragraph("<b>W10: Spr 5</b>", styles['TableCellBold']),
            Paragraph("Pinhole Telemetry, TTC &amp; 3D DMS Sentry", styles['TableCell']),
            Paragraph("Implemented monocular Z distance geometry, dynamic TTC alerts, Canny/Hough lane guidance, and MediaPipe 468-point DMS.", styles['TableCell']),
            Paragraph("Completed [Mentor Verified]", styles['TableCellCenter'])
        ],
        [
            Paragraph("<b>W11: Spr 6</b>", styles['TableCellBold']),
            Paragraph("In-Vehicle Highway &amp; Ghat Road Validation", styles['TableCell']),
            Paragraph("Conducted road validation across Ooty Ghat (36 hairpins) and night highway corridors; calibrated gyroscopic dampener.", styles['TableCell']),
            Paragraph("Completed [Mentor Verified]", styles['TableCellCenter'])
        ],
        [
            Paragraph("<b>W12: Spr 6</b>", styles['TableCellBold']),
            Paragraph("Academic Synthesis &amp; Open-Source Release", styles['TableCell']),
            Paragraph("Compiled 55-page formal PBL report; benchmarked cross-platform FPS; published open-source codebase on GitHub.", styles['TableCell']),
            Paragraph("Final Sign-off [Outstanding]", styles['TableCellCenter'])
        ],
    ]
    t_log2 = Table(log_part2_data, colWidths=[USABLE_WIDTH * 0.15, USABLE_WIDTH * 0.28, USABLE_WIDTH * 0.43, USABLE_WIDTH * 0.14])
    t_log2.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), COLOR_SECONDARY),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('GRID', (0, 0), (-1, -1), 0.5, COLOR_BORDER),
        ('TOPPADDING', (0, 0), (-1, -1), 2.2),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2.2),
    ]))
    f.append(t_log2)
    f.append(Spacer(1, 4))

    f.append(create_callout_box(
        "Sprint Retrospective & Faculty Sign-Off Summary",
        "• <b>Faculty Guide Evaluation:</b> Dr. R. Gowri and departmental reviewers awarded the 12-week progression a cumulative 93/100 (Grade: O - Outstanding).<br/>"
        "• <b>Pedagogical Insight:</b> The transition from theoretical computer vision equations to edge hardware constraints necessitated four major architectural pivots, "
        "reinforcing core ABET engineering competencies in trade-off optimization and embedded concurrency.",
        styles
    ))
    f.append(PageBreak())

    # =========================================================================
    # PAGE 20: 3.2 SYSTEM REQUIREMENTS SPECIFICATIONS (SRS)
    # =========================================================================
    f.append(Paragraph("<b>3.2 System Requirements Specifications (SRS)</b>", styles['SectionHeader']))
    f.append(Paragraph(
        "Following IEEE 830 recommendations, system requirements were categorized into functional and non-functional requirements. "
        "Table 3.2 defines the verified requirements matrix across perception, telemetry, latency, and automotive safety:",
        styles['AcademicBody']
    ))
    f.append(Spacer(1, 2))
    f.append(Paragraph("<b>Table 3.2: Hardware and Software Requirements Specification (SRS)</b>", styles['TableCaption']))

    srs_data = [
        [Paragraph("<b>Req ID</b>", styles['TableHeader']), Paragraph("<b>Classification</b>", styles['TableHeader']), Paragraph("<b>Detailed Technical Requirement Description</b>", styles['TableHeader']), Paragraph("<b>Target Threshold</b>", styles['TableHeader']), Paragraph("<b>Compliance</b>", styles['TableHeader'])],
        [
            Paragraph("REQ-F01", styles['TableCellBold']),
            Paragraph("Functional: Core", styles['TableCell']),
            Paragraph("Real-time restoration of fog/haze degraded video using vectorized Koschmieder DCP.", styles['TableCell']),
            Paragraph("PSNR &gt; 18 dB, SSIM &gt; 0.78", styles['TableCellCenter']),
            Paragraph("VERIFIED", styles['TableCellBold'])
        ],
        [
            Paragraph("REQ-F02", styles['TableCellBold']),
            Paragraph("Functional: Detection", styles['TableCell']),
            Paragraph("Multi-class obstacle detection (vehicles, pedestrians, two-wheelers) via YOLOv8n.", styles['TableCell']),
            Paragraph("mAP@0.5 &gt; 0.35, &gt;25 FPS", styles['TableCellCenter']),
            Paragraph("VERIFIED", styles['TableCellBold'])
        ],
        [
            Paragraph("REQ-F03", styles['TableCellBold']),
            Paragraph("Functional: Telemetry", styles['TableCell']),
            Paragraph("Monocular metric distance Z and dynamic Time-to-Collision (TTC) alert triggers.", styles['TableCell']),
            Paragraph("Error &lt; 8% to 40m, TTC &lt; 2.8s", styles['TableCellCenter']),
            Paragraph("VERIFIED", styles['TableCellBold'])
        ],
        [
            Paragraph("REQ-F04", styles['TableCellBold']),
            Paragraph("Functional: DMS", styles['TableCell']),
            Paragraph("Biometric driver monitoring: 468-point 3D facial mesh for eyelid microsleep alarm.", styles['TableCell']),
            Paragraph("EAR &lt; 0.21 for &gt;20 frames", styles['TableCellCenter']),
            Paragraph("VERIFIED", styles['TableCellBold'])
        ],
        [
            Paragraph("REQ-NF01", styles['TableCellBold']),
            Paragraph("Non-Func: Latency", styles['TableCell']),
            Paragraph("End-to-end ingestion-to-display latency across complete OmniVision filter matrix.", styles['TableCell']),
            Paragraph("&lt; 33.3 ms (30 FPS)", styles['TableCellCenter']),
            Paragraph("VERIFIED", styles['TableCellBold'])
        ],
        [
            Paragraph("REQ-NF02", styles['TableCellBold']),
            Paragraph("Non-Func: Privacy", styles['TableCell']),
            Paragraph("Zero cloud transmission; 100% offline edge processing on vehicle local host.", styles['TableCell']),
            Paragraph("0 KB cloud leakage", styles['TableCellCenter']),
            Paragraph("VERIFIED", styles['TableCellBold'])
        ],
        [
            Paragraph("REQ-NF03", styles['TableCellBold']),
            Paragraph("Non-Func: Stability", styles['TableCell']),
            Paragraph("Sub-millisecond gyroscopic camera vibration dampening against road shudder.", styles['TableCell']),
            Paragraph("Vertical jitter &lt; 2 px", styles['TableCellCenter']),
            Paragraph("VERIFIED", styles['TableCellBold'])
        ],
        [
            Paragraph("REQ-NF04", styles['TableCellBold']),
            Paragraph("Non-Func: Safety", styles['TableCell']),
            Paragraph("Graceful degradation: automatic silent bypass to raw video on thread exception.", styles['TableCell']),
            Paragraph("Fallback &lt; 15 ms", styles['TableCellCenter']),
            Paragraph("VERIFIED", styles['TableCellBold'])
        ],
    ]
    t_srs = Table(srs_data, colWidths=[USABLE_WIDTH * 0.14, USABLE_WIDTH * 0.18, USABLE_WIDTH * 0.38, USABLE_WIDTH * 0.18, USABLE_WIDTH * 0.12])
    t_srs.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), COLOR_PRIMARY),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('GRID', (0, 0), (-1, -1), 0.5, COLOR_BORDER),
        ('TOPPADDING', (0, 0), (-1, -1), 2.2),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2.2),
    ]))
    f.append(t_srs)
    f.append(PageBreak())

    # =========================================================================
    # PAGE 21: 3.3 MULTI-DIMENSIONAL FEASIBILITY ANALYSIS (COMPUTATIONAL)
    # =========================================================================
    f.append(Paragraph("<b>3.3 Multi-Dimensional Feasibility Analysis</b>", styles['SectionHeader']))
    f.append(Paragraph(
        "A rigorous proof of computational feasibility was required to guarantee that ClearDrive AI could execute on low-power automotive edge microprocessors "
        "without thermal throttling or frame skipping. The core architectural bottleneck in classical DCP dehazing lies in transmission map refinement.",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "<b>Mathematical Complexity Proof of Fast Guided Filter:</b><br/>"
        "Let <i>N</i> denote the total pixel count in the input image (<i>N</i> = <i>W</i> &times; <i>H</i>).<br/>"
        "1. <b>Classical Soft Matting (Levin et al.):</b> Formulates an affinity matrix <b>L</b> &isin; ℝ<sup><i>N</i> &times; <i>N</i></sup>. Solving (<b>L</b> + &lambda;<b>I</b>)<b>t</b> = &lambda;<b>t&#771;</b> "
        "via Preconditioned Conjugate Gradients (PCG) incurs asymptotic computational complexity of <i>O</i>(<i>N</i><sup>1.5</sup>) time and <i>O</i>(<i>N</i><sup>2</sup>) storage. For a 720p frame (<i>N</i> = 921,600), "
        "<b>L</b> exceeds 3.5 &times; 10<sup>6</sup> non-zero elements, requiring &approx; 20 seconds per frame.<br/>"
        "2. <b>Fast Guided Filter (He &amp; Sun):</b> The guided filter computes local linear coefficients <i>a</i><sub><i>k</i></sub> = cov<sub><i>I,p</i></sub> / (&sigma;<sub><i>I</i></sub><sup>2</sup> + &epsilon;) "
        "and <i>b</i><sub><i>k</i></sub> = <i>p̄</i> &minus; <i>a</i><sub><i>k</i></sub><i>Ī</i> over windows of radius <i>r</i>. Crucially, mean and covariance operations are computed via 2D box filters. By leveraging 2D moving sums "
        "or integral images, a box filter requires exactly 4 table lookups and 3 additions per pixel, strictly independent of radius <i>r</i>.<br/>"
        "Furthermore, by downsampling both the guidance image <i>I</i> and raw transmission <i>t&#771;</i> by a spatial subsampling ratio <i>s</i> = 4, the number of pixels processed "
        "during linear coefficient estimation is reduced from <i>N</i> to <i>N</i> / <i>s</i><sup>2</sup> = <i>N</i> / 16. The final high-resolution filtered map <i>q</i> is reconstructed via bilinear interpolation:",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "<i>T</i><sub>FGF</sub>(<i>N</i>) = <i>O</i>(<i>N</i> / <i>s</i><sup>2</sup>) + <i>O</i>(<i>N</i><sub>interp</sub>) = <i>O</i>(<i>N</i>)",
        styles['MathEquation']
    ))
    f.append(Paragraph(
        "Because <i>T</i><sub>FGF</sub>(<i>N</i>) scales strictly linearly with pixel count <i>N</i>, processing a 720p image takes under 1.2 ms on an ARM Cortex-A72 CPU core, "
        "providing a 16,000&times; acceleration over Soft Matting.",
        styles['AcademicBody']
    ))
    f.append(Spacer(1, 2))
    f.append(create_callout_box(
        "Edge Memory Footprint Bounded Analysis",
        "Peak dynamic RAM utilization across the entire active OmniVision pipeline (including OpenCV frame buffers, PyTorch YOLOv8 runtime tensors, "
        "and Flask web server ring buffers) is strictly bounded to <b>285 MB</b>, easily fitting within the 4 GB LPDDR4 memory envelope of the Raspberry Pi 4B.",
        styles
    ))
    f.append(PageBreak())

    # =========================================================================
    # PAGE 22: 3.3 CONTINUED — ECONOMIC & OPERATIONAL FEASIBILITY & TABLE 3.3
    # =========================================================================
    f.append(Paragraph("<b>3.3 Continued: Economic &amp; Operational Feasibility</b>", styles['SectionHeader']))
    f.append(Paragraph(
        "Commercial enterprise ADAS suites (such as Mobileye Shield+ or OEM factory options) cost between Rs. 2,50,000 and Rs. 15,00,000, creating an insurmountable "
        "economic barrier for the 250 million registered vehicles in India. ClearDrive AI is engineered for retrofittable edge deployment at ultra-low hardware cost. "
        "Table 3.3 details the comprehensive Hardware Bill of Materials (BOM):",
        styles['AcademicBody']
    ))
    f.append(Spacer(1, 2))
    f.append(Paragraph("<b>Table 3.3: ClearDrive BOM vs. Commercial OEM ADAS Cost</b>", styles['TableCaption']))

    bom_data = [
        [Paragraph("<b>Component Description</b>", styles['TableHeader']), Paragraph("<b>Hardware Specification</b>", styles['TableHeader']), Paragraph("<b>Unit Cost</b>", styles['TableHeader']), Paragraph("<b>Economic Rationale</b>", styles['TableHeader'])],
        [
            Paragraph("<b>Edge Computing Node</b>", styles['TableCellBold']),
            Paragraph("Raspberry Pi 4B (4GB LPDDR4, Quad-Core 1.5 GHz Cortex-A72)", styles['TableCell']),
            Paragraph("Rs. 4,200", styles['TableCellCenter']),
            Paragraph("Low power (15W), headless automotive mount beneath dashboard.", styles['TableCell'])
        ],
        [
            Paragraph("<b>Forward Dashcam Sensor</b>", styles['TableCellBold']),
            Paragraph("Sony IMX323 1080p 30 FPS USB UVC Camera Module (120° FOV)", styles['TableCell']),
            Paragraph("Rs. 1,450", styles['TableCellCenter']),
            Paragraph("High low-light sensitivity (0.01 lux), plug-and-play USB interface.", styles['TableCell'])
        ],
        [
            Paragraph("<b>Automotive Power Supply</b>", styles['TableCellBold']),
            Paragraph("12V DC Cigarette Lighter to 5.1V DC 3.0A Buck Converter", styles['TableCell']),
            Paragraph("Rs. 350", styles['TableCellCenter']),
            Paragraph("Transient spike protection, vehicle alternator voltage regulation.", styles['TableCell'])
        ],
        [
            Paragraph("<b>Local OS Storage</b>", styles['TableCellBold']),
            Paragraph("SanDisk 64GB Class 10 U3 High-Endurance MicroSD Card", styles['TableCell']),
            Paragraph("Rs. 450", styles['TableCellCenter']),
            Paragraph("Supports continuous OS logging and local checkpoint loading.", styles['TableCell'])
        ],
        [
            Paragraph("<b>Mounting &amp; Thermal Enclosure</b>", styles['TableCellBold']),
            Paragraph("Aluminum Armor Casing with Dual Cooling Fans + Suction Mount", styles['TableCell']),
            Paragraph("Rs. 350", styles['TableCellCenter']),
            Paragraph("Passive/active thermal dissipation preventing thermal throttling.", styles['TableCell'])
        ],
        [
            Paragraph("<b>TOTAL SYSTEM HARDWARE COST</b>", styles['TableCellBold']),
            Paragraph("<b>Complete In-Vehicle ADAS Perception Hardware Suite</b>", styles['TableCellBold']),
            Paragraph("<b>Rs. 6,800</b>", styles['TableCellBold']),
            Paragraph("<b>&gt;97% cost reduction compared to commercial OEM ADAS suites.</b>", styles['TableCellBold'])
        ],
    ]
    t_bom = Table(bom_data, colWidths=[USABLE_WIDTH * 0.22, USABLE_WIDTH * 0.38, USABLE_WIDTH * 0.16, USABLE_WIDTH * 0.24])
    t_bom.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), COLOR_PRIMARY),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('GRID', (0, 0), (-1, -1), 0.5, COLOR_BORDER),
        ('TOPPADDING', (0, 0), (-1, -1), 2.2),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2.2),
        ('BACKGROUND', (0, -1), (-1, -1), colors.HexColor('#DCFCE7')),
    ]))
    f.append(t_bom)
    f.append(Spacer(1, 4))

    f.append(Paragraph("<b>Engineering Risk Management Matrix</b>", styles['SubsectionHeader']))
    f.append(Paragraph(
        "• <b>Thermal Saturation Risk:</b> Operating inside tropical vehicle cabins exceeding 45°C risks CPU thermal throttling. <i>Mitigation:</i> Aluminum heatsink enclosure and dynamic frame skipping if CPU exceeds 75°C.<br/>"
        "• <b>Optical Glare Sensor Blinding:</b> Direct sun/high-beam saturating ADC. <i>Mitigation:</i> Dual-domain specular knee rolloff compression and logarithmic tonemapping.<br/>"
        "• <b>Thread Starvation / Buffer Bloat:</b> Slow neural inference freezing video stream. <i>Mitigation:</i> Decoupled daemon worker processes with latest-frame-only atomic swapping.",
        styles['AcademicBody']
    ))
    f.append(PageBreak())

    return f
