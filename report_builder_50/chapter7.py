"""
Chapter 7: Team Reflection and Learning Outcomes (Pages 44 to 46 - Exactly 3 Pages)
ClearDrive AI: Real-Time ADAS and Vision Restoration for Adverse Driving Conditions
"""

from reportlab.platypus import Paragraph, Spacer, Table, TableStyle, PageBreak, HRFlowable
from reportlab.lib import colors
from report_builder_50.styles import (
    USABLE_WIDTH, COLOR_PRIMARY, COLOR_SECONDARY, COLOR_BORDER,
    create_callout_box
)


def get_chapter7_flowables(styles):
    """Returns flowables for Chapter 7 (Pages 44 to 46 - Exactly 3 Pages)."""
    f = []

    # =========================================================================
    # PAGE 44: CHAPTER 7 COVER & 7.1 SHIVANESH V REFLECTION
    # =========================================================================
    f.append(Paragraph("<b>CHAPTER 7</b>", styles['ChapterHeader']))
    f.append(Paragraph("<b>TEAM REFLECTION AND LEARNING OUTCOMES</b>", styles['DocTitle']))
    f.append(HRFlowable(width="100%", thickness=1.2, color=COLOR_PRIMARY, spaceBefore=2, spaceAfter=8))

    f.append(Paragraph("<b>7.1 Individual Reflection: Lead Systems &amp; AI Engineer (Shivanesh V)</b>", styles['SectionHeader']))
    f.append(Paragraph(
        "Leading the systems engineering, embedded concurrency, and machine learning telemetry on ClearDrive AI has been a transformative engineering journey. "
        "Prior to this project, my understanding of machine learning was largely confined to offline Jupyter notebooks and static benchmarking on curated datasets. "
        "ClearDrive AI fundamentally dismantled that sanitized perspective, forcing me to confront the brutal operational realities of real-time embedded edge computing.",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "<b>Architectural Leadership &amp; Concurrency:</b> My primary engineering responsibility was architecting the end-to-end edge pipeline and resolving the "
        "catastrophic 1.8 FPS choke that paralyzed Iteration 1. Diagnosing how the Python Global Interpreter Lock (GIL) and synchronous camera capture caused "
        "massive buffer bloat-lagging video display by over 18 seconds-was a defining crucible. By decoupling video ingestion, optical restoration, neural inference, "
        "and HTTP streaming into dedicated multi-core multiprocessing worker pools with lock-free atomic shared memory buffers, I unlocked a <b>2,300% throughput increase</b>, "
        "scaling the system to 38.6 FPS on x86 and 32.4 FPS on the Raspberry Pi 4B.",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "<b>Neural Kinematics &amp; Ground Geometry:</b> Translating raw YOLOv8 bounding boxes into safety-critical telemetry required deep mathematical synthesis. "
        "I formulated the monocular pinhole distance geometry and dynamic Time-to-Collision (TTC) kinematics, engineering exponential distance smoothing filters "
        "that reduced telemetry jitter from +/-40% down to under 5%. Furthermore, I implemented the sub-millisecond gyroscopic 1D projection correlation dampener, "
        "ensuring telemetry stayed rock-steady even when driving over rough mountain ghat cobblestones.",
        styles['AcademicBody']
    ))
    f.append(Spacer(1, 4))
    f.append(create_callout_box(
        "Key Engineering Takeaway - Shivanesh V",
        "&quot;In safety-critical autonomous systems, algorithmic accuracy without deterministic low latency is lethal. "
        "True engineering excellence lies not in choosing the largest neural model, but in optimizing lightweight models "
        "and concurrency architectures that reliably deliver within strict 33 ms hardware deadlines.&quot;",
        styles
    ))
    f.append(PageBreak())

    # =========================================================================
    # PAGE 45: 7.2 CO-RESEARCHER REFLECTION & TEAM DYNAMICS
    # =========================================================================
    f.append(Paragraph("<b>7.2 Individual Reflection: CV &amp; DSP Specialist (Co-Researcher) &amp; Team Synergy</b>", styles['SectionHeader']))
    f.append(Paragraph(
        "My primary technical domain encompassed atmospheric scattering physics, image restoration digital signal processing, roadway geometric perception, "
        "and biometric driver vigilance monitoring. This project taught me that textbook computer vision algorithms rarely survive real-world deployment without "
        "deep mathematical adaptation.",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "<b>Overcoming the Tree Bug &amp; Fast Guided Filter:</b> When our initial Levin Soft Matting implementation exhausted system RAM and stalled at 1.8 FPS, "
        "I led the mathematical pivot to He and Sun's Fast Guided Filter. Vectorizing box filter running sums in NumPy and OpenCV achieved an astonishing "
        "$16,000\\times$ acceleration. Subsequently, when mountain road tests revealed the infamous 'Tree Bug'-where dark foliage caused blinding white halo artifacts-"
        "I derived the mathematical proof showing that near-zero dark foliage pixel intensities caused the transmission denominator to collapse. Formulating the "
        "adaptive luminance transmission floor $t_0(x)$ and first-order EMA airlight smoothing completely eradicated the Tree Bug and sky flickering.",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "<b>Multi-Modal Safety &amp; Biometrics:</b> I engineered the AR neon-cyan lane projection, HSV foliage-filtered pothole depth scanner, and the 468-point "
        "MediaPipe facial mesh DMS that monitors eyelid Eye Aspect Ratio (EAR) to detect microsleep events in &lt;3.5 ms on CPU.",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "<b>Team Dynamics and Collaborative Synergy:</b> The division of labor between Systems Architecture (Shivanesh V) and Optical DSP (Co-Researcher) was "
        "cleanly demarcated yet intensely collaborative. Daily standups, rigorous branch reviews, and shared in-vehicle testing sessions enabled us to resolve "
        "complex multidisciplinary bugs rapidly. Working as a cohesive pair transformed a daunting 12-week challenge into an outstanding research triumph.",
        styles['AcademicBody']
    ))
    f.append(PageBreak())

    # =========================================================================
    # PAGE 46: 7.3 COURSE OUTCOME ATTAINMENT & PO/PSO MAPPING MATRIX
    # =========================================================================
    f.append(Paragraph("<b>7.3 Course Outcome (CO) Attainment &amp; PO/PSO Mapping Matrix</b>", styles['SectionHeader']))
    f.append(Paragraph(
        "In strict alignment with the Project-Based Learning curriculum guidelines of Chennai Institute of Technology and NBA/ABET engineering criteria, "
        "Table 7.1 documents the systematic attainment of Course Outcomes (CO1 to CO6) and their mapping to Program Outcomes (POs) and Program Specific Outcomes (PSOs):",
        styles['AcademicBody']
    ))
    f.append(Spacer(1, 2))

    co_data = [
        [Paragraph("<b>Course Outcome (CO)</b>", styles['TableHeader']), Paragraph("<b>Statement of Competency Attained</b>", styles['TableHeader']), Paragraph("<b>Mapped POs / PSOs</b>", styles['TableHeader']), Paragraph("<b>Level</b>", styles['TableHeader'])],
        [
            Paragraph("<b>CO1: Physical Modeling</b>", styles['TableCellBold']),
            Paragraph("Formulate and analyze mathematical models of atmospheric scattering, Koschmieder optical physics, and dark channel priors.", styles['TableCell']),
            Paragraph("PO1 (Engg Knowledge), PO2 (Problem Analysis)", styles['TableCell']),
            Paragraph("<b>Level 3 (High)</b>", styles['TableCellCenter'])
        ],
        [
            Paragraph("<b>CO2: DSP &amp; Algorithm Optimization</b>", styles['TableCellBold']),
            Paragraph("Design and implement vectorized linear-time image restoration algorithms (Fast Guided Filter, CLAHE, Anti-glare) for real-time edge processing.", styles['TableCell']),
            Paragraph("PO3 (Design/Dev), PO5 (Modern Tool Usage)", styles['TableCell']),
            Paragraph("<b>Level 3 (High)</b>", styles['TableCellCenter'])
        ],
        [
            Paragraph("<b>CO3: Neural Kinematics &amp; Telemetry</b>", styles['TableCellBold']),
            Paragraph("Integrate quantized deep neural networks with geometric monocular telemetry for obstacle kinematics, distance Z, and dynamic TTC.", styles['TableCell']),
            Paragraph("PO3 (Design/Dev), PO4 (Complex Investigation)", styles['TableCell']),
            Paragraph("<b>Level 3 (High)</b>", styles['TableCellCenter'])
        ],
        [
            Paragraph("<b>CO4: Embedded Concurrency &amp; Safety</b>", styles['TableCellBold']),
            Paragraph("Architect lock-free multiprocessing pipelines and biometric driver monitoring (DMS) adhering to AIS-140/145 safety standards.", styles['TableCell']),
            Paragraph("PO3 (Design/Dev), PO6 (Engineer &amp; Society)", styles['TableCell']),
            Paragraph("<b>Level 3 (High)</b>", styles['TableCellCenter'])
        ],
        [
            Paragraph("<b>CO5: Experimental Validation</b>", styles['TableCellBold']),
            Paragraph("Rigorously validate system performance across real-world adverse weather scenarios (fog, rain, night, glare) and low-cost edge SBC hardware.", styles['TableCell']),
            Paragraph("PO4 (Investigation), PO5 (Tool Usage), PSO1", styles['TableCell']),
            Paragraph("<b>Level 3 (High)</b>", styles['TableCellCenter'])
        ],
        [
            Paragraph("<b>CO6: Professional Ethics &amp; Teamwork</b>", styles['TableCellBold']),
            Paragraph("Demonstrate collaborative Agile teamwork, professional documentation, open-source dissemination, and societal impact.", styles['TableCell']),
            Paragraph("PO9 (Teamwork), PO10 (Communication), PO12", styles['TableCell']),
            Paragraph("<b>Level 3 (High)</b>", styles['TableCellCenter'])
        ],
    ]
    t_co = Table(co_data, colWidths=[USABLE_WIDTH * 0.22, USABLE_WIDTH * 0.44, USABLE_WIDTH * 0.22, USABLE_WIDTH * 0.12])
    t_co.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), COLOR_PRIMARY),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('GRID', (0, 0), (-1, -1), 0.5, COLOR_BORDER),
        ('TOPPADDING', (0, 0), (-1, -1), 2.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2.5),
        ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#F8FAFC')),
    ]))
    f.append(t_co)
    f.append(Spacer(1, 4))
    f.append(Paragraph(
        "<b>Attainment Summary:</b> The project attained maximum Level 3 (Substantial / High) mapping across all six Course Outcomes, "
        "fulfilling both the Machine Learning curriculum requirements and ABET accreditation standards for capstone engineering excellence.",
        styles['AcademicBody']
    ))
    f.append(PageBreak())

    return f
