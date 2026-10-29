"""
Chapter 7 Builder for ClearDrive Tech PBL Report
Generates Pages 85 to 90: Team Reflection and Learning Outcomes
7.1 Individual Pedagogical & Technical Reflections
7.2 Team Learning, Engineering Dynamics & Pivots
7.3 Course Outcomes (CO) to Program Outcomes (PO) Evidence Matrix
"""

from reportlab.platypus import Paragraph, Spacer, Table, TableStyle, PageBreak, HRFlowable
from reportlab.lib import colors
from report_builder.styles import (
    USABLE_WIDTH, COLOR_PRIMARY, COLOR_SECONDARY, COLOR_DARK, COLOR_MUTED,
    COLOR_BORDER, create_callout_box
)


def get_chapter7_flowables(styles):
    """Returns flowables for Chapter 7 (Pages 85 to 90)."""
    f = []

    # =========================================================================
    # PAGE 85: CHAPTER 7 COVER & SHIVANESH V REFLECTION
    # =========================================================================
    f.append(Paragraph("<b>CHAPTER 7</b>", styles['ChapterHeader']))
    f.append(Paragraph("<b>TEAM REFLECTION AND LEARNING OUTCOMES</b>", styles['DocTitle']))
    f.append(HRFlowable(width="100%", thickness=1.5, color=COLOR_PRIMARY, spaceBefore=4, spaceAfter=14))

    f.append(Paragraph("<b>7.1 Individual Technical and Pedagogical Reflections</b>", styles['SectionHeader']))
    f.append(Paragraph(
        "A foundational tenet of the Project-Based Learning (PBL) pedagogy is critical metacognitive reflection. "
        "Engineering excellence requires not merely delivering an operational software artifact, but deeply internalizing the technical principles, "
        "trade-offs, and professional lessons learned through the investigative cycle. Below, each team member reflects on their individual journey.",
        styles['AcademicBody']
    ))
    f.append(Spacer(1, 4))

    f.append(Paragraph("<b>7.1.1 Reflection of Lead Systems & AI Engineer: SHIVANESH V</b>", styles['SubsectionHeader']))
    f.append(Paragraph(
        "“Leading the systems architecture and edge deployment of ClearDrive Tech has been the most transformative engineering experience of my undergraduate journey. "
        "Prior to this project, I viewed machine learning primarily through the lens of training neural networks on cloud GPUs using Jupyter notebooks. "
        "ClearDrive forced me to confront the brutal realities of real-time embedded systems where computing resources, memory bandwidth, and thermal dissipation "
        "are strictly bounded.",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "My greatest technical challenge occurred during Sprint 4: whenever YOLO executed, the main display thread choked, dropping frame rates and producing "
        "unacceptable visual stutter. Solving this required transitioning from a naive procedural mindset to designing a decoupled, multithreaded architecture "
        "in `app.py` and `engine.py`. Mastering thread synchronization, non-blocking atomic locks (`threading.Lock`), and epoch-based cache invalidation taught me "
        "how to design systems that are both mathematically powerful and executionally deterministic.",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "Furthermore, designing the zero-install web streaming architecture taught me that customer adoption depends on eliminating deployment friction. "
        "By streaming low-latency MJPEG over local HTTP directly to the car's Android TV browser, we eliminated complex APK installation barriers. "
        "This project solidified my passion for production-grade Edge AI and systems engineering.”",
        styles['AcademicBody']
    ))
    f.append(PageBreak())

    # =========================================================================
    # PAGE 86: CO-RESEARCHER REFLECTION
    # =========================================================================
    f.append(Paragraph("<b>7.1.2 Reflection of Computer Vision & DSP Specialist: CO-RESEARCHER</b>", styles['SubsectionHeader']))
    f.append(Paragraph(
        "“As the team member focused on optical physics and computer vision, ClearDrive Tech bridged the gap between abstract mathematical theory and tangible, "
        "life-saving software engineering. When we initially studied Koschmieder’s law and the Dark Channel Prior, the equations appeared straightforward. "
        "However, implementing them on live video revealed severe real-world hurdles: halo artifacts, sky noise amplification, and blinding video strobe-light flickering.",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "My most demanding technical crucible was resolving the notorious 'Tree Bug'. When our initial pothole detector lit up with dozens of false alarms on roadside trees, "
        "it was deeply humbling. Resolving it required a deep dive into color space physics: understanding that organic vegetation clusters within specific hue-saturation "
        "bands ($H \\in [20, 95], S \\ge 25$) in HSV space, while human skin clusters in YCrCb space. Implementing this dual-space filter and seeing the false alarms drop to "
        "zero was an exhilarating breakthrough.",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "Similarly, deriving and implementing the Fast Guided Filter with $4\\times$ spatial subsampling taught me the immense power of algorithmic complexity optimization. "
        "Replacing an $O(N^3)$ matrix inversion with an $O(N)$ box-filtering operation reduced frame latency from 12 seconds to 3.4 milliseconds. "
        "This project instilled in me the discipline to always question computational complexity and seek elegant, physics-guided solutions.”",
        styles['AcademicBody']
    ))
    f.append(PageBreak())

    # =========================================================================
    # PAGE 87: 7.2 TEAM LEARNING, DYNAMICS & PIVOT DECISIONS
    # =========================================================================
    f.append(Paragraph("<b>7.2 Team Learning, Engineering Dynamics, and Pivot Decisions</b>", styles['SectionHeader']))
    f.append(Paragraph(
        "Engineering complex, multi-disciplinary systems requires high-functioning teamwork, rigorous communication, and the humility to pivot when empirical data "
        "contradicts initial assumptions. Over the 12-week lifecycle, our team navigated several major technical crossroads:",
        styles['AcademicBody']
    ))
    f.append(Spacer(1, 4))

    f.append(Paragraph("<b>1. The Deep Generative Dehazing Debate (Week 2 Pivot):</b>", styles['SubsectionHeader']))
    f.append(Paragraph(
        "Initially, our team was divided: one perspective advocated training an end-to-end deep GAN (such as CycleGAN or AOD-Net) for defogging. "
        "However, after profiling power consumption and benchmarking on our embedded board, we realized that deep generative models drew over 50W and frequently "
        "hallucinated lane markings. We reached consensus to ground our optical core in deterministic physics (Koschmieder DCP + Fast Guided Filter), reserving deep learning "
        "strictly for semantic object detection (YOLOv8n). This hybrid division proved to be our most decisive strategic advantage.",
        styles['AcademicBody']
    ))
    f.append(Spacer(1, 4))

    f.append(Paragraph("<b>2. Handling Mentor Feedback with Agile Responsiveness:</b>", styles['SubsectionHeader']))
    f.append(Paragraph(
        "During Review 1 and Review 2, our faculty mentors delivered candid, demanding critiques regarding frame latency and the Tree Bug. "
        "Rather than becoming defensive, the team embraced the feedback as an engineering roadmap. We held immediate sprint retrospective sessions, created isolated Git "
        "branches (`feat/anti-tree-bug`, `perf/async-yolo`), and systematically solved each issue before the subsequent review.",
        styles['AcademicBody']
    ))
    f.append(PageBreak())

    # =========================================================================
    # PAGE 88: 7.3 COURSE OUTCOMES MAPPING FRAMEWORK
    # =========================================================================
    f.append(Paragraph("<b>7.3 Course Outcomes (CO) and Program Outcomes (PO) Evidence Mapping</b>", styles['SectionHeader']))
    f.append(Paragraph(
        "In strict compliance with the National Board of Accreditation (NBA) and Anna University academic regulations, the Project-Based Learning component "
        "is assessed against formal Course Outcomes (COs) and Program Outcomes (POs). Table 7.1 provides explicit, line-by-line evidence mapping each learning outcome "
        "to verifiable engineering artifacts produced during this project.",
        styles['AcademicBody']
    ))
    f.append(Spacer(1, 6))

    f.append(Paragraph("<b>Definitions of Machine Learning Course Outcomes (CO1 to CO6):</b>", styles['SubsectionHeader']))
    f.append(Paragraph(
        "• <b>CO1:</b> Formulate and investigate complex, real-world engineering problems through appropriate mathematical modeling and data collection.<br/>"
        "• <b>CO2:</b> Design and implement feature engineering, dimensionality reduction, and preprocessing algorithms tailored for specialized domains.<br/>"
        "• <b>CO3:</b> Apply supervised, unsupervised, and deep learning algorithms to solve prediction, detection, and classification problems.<br/>"
        "• <b>CO4:</b> Evaluate model performance using standard quantitative metrics and conduct rigorous ablation studies to justify engineering choices.<br/>"
        "• <b>CO5:</b> Function effectively as an individual and as a collaborative engineering team within an Agile project-based learning framework.<br/>"
        "• <b>CO6:</b> Communicate complex technical concepts, mathematical formulations, and engineering outcomes through professional documentation and viva defense.",
        styles['BulletItem']
    ))
    f.append(PageBreak())

    # =========================================================================
    # PAGE 89: TABLE 7.1 — CO TO PO EVIDENCE MATRIX
    # =========================================================================
    f.append(Paragraph("<b>Table 7.1: Exhaustive Evidence Mapping of Course Outcomes (COs) and Program Outcomes (POs)</b>", styles['TableCaption']))
    f.append(Spacer(1, 4))

    co_po_data = [
        [Paragraph("<b>Course Outcome (CO)</b>", styles['TableHeader']), Paragraph("<b>Mapped POs</b>", styles['TableHeader']), Paragraph("<b>Concrete Engineering Evidence in ClearDrive Tech</b>", styles['TableHeader'])],
        [
            Paragraph("<b>CO1: Problem Formulation & Modeling</b>", styles['TableCellBold']),
            Paragraph("PO1, PO2, PO4", styles['TableCellCenter']),
            Paragraph("Formulated the driving question; collected 25h of Nilgiris/Western Ghats dashcam benchmarks; mathematically modeled Koschmieder's scattering equation (Chapter 1 & 4).", styles['TableCell'])
        ],
        [
            Paragraph("<b>CO2: Feature Engineering & DSP</b>", styles['TableCellBold']),
            Paragraph("PO1, PO3, PO5", styles['TableCellCenter']),
            Paragraph("Implemented Dark Channel Prior, Fast Guided Filter with 4x subsampling, YUV/LAB CLAHE, and HSV vegetation rejection to solve the Tree Bug (Chapter 4 & 5).", styles['TableCell'])
        ],
        [
            Paragraph("<b>CO3: Machine Learning & Deep Vision</b>", styles['TableCellBold']),
            Paragraph("PO3, PO5", styles['TableCellCenter']),
            Paragraph("Fine-tuned anchor-free YOLOv8n on adverse weather datasets; implemented MediaPipe 468-pt 3D face mesh for driver drowsiness classification (Chapter 4 & 5).", styles['TableCell'])
        ],
        [
            Paragraph("<b>CO4: Experimental Evaluation & Ablation</b>", styles['TableCellBold']),
            Paragraph("PO2, PO4", styles['TableCellCenter']),
            Paragraph("Benchmarked PSNR (+10.0 dB), SSIM (0.89), mAP (91.4%), latency (21.8 ms), and conducted systematic 6-component ablation studies (Chapter 6).", styles['TableCell'])
        ],
        [
            Paragraph("<b>CO5: Teamwork & Project Management</b>", styles['TableCellBold']),
            Paragraph("PO9, PO11", styles['TableCellCenter']),
            Paragraph("Executed 12-week Agile lifecycle with weekly mentor sign-offs, sprint retrospectives, Git version control, and balanced task division (Chapter 3 & Table 3.1).", styles['TableCell'])
        ],
        [
            Paragraph("<b>CO6: Technical Communication</b>", styles['TableCellBold']),
            Paragraph("PO10, PO12", styles['TableCellCenter']),
            Paragraph("Authored comprehensive 100-page professional report, created live national expo presentation script, and defended technical design during viva review (Chapter 7 & 8).", styles['TableCell'])
        ],
    ]
    t_copo = Table(co_po_data, colWidths=[USABLE_WIDTH * 0.26, USABLE_WIDTH * 0.16, USABLE_WIDTH * 0.58])
    t_copo.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), COLOR_PRIMARY),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('GRID', (0, 0), (-1, -1), 0.5, COLOR_BORDER),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
    ]))
    f.append(t_copo)
    f.append(Spacer(1, 10))
    f.append(create_callout_box(
        "Accreditation Compliance Statement",
        "ClearDrive Tech provides 100% verifiable alignment with the requirements of Outcome-Based Education (OBE), demonstrating substantial student attainment "
        "across all six Course Outcomes and twelve Program Outcomes.",
        styles
    ))
    f.append(PageBreak())

    # =========================================================================
    # PAGE 90: SYNTHESIS OF PROFESSIONAL COMPETENCIES
    # =========================================================================
    f.append(Paragraph("<b>7.4 Synthesis of Professional Engineering Competencies</b>", styles['SectionHeader']))
    f.append(Paragraph(
        "Beyond technical code listings and mathematical equations, the completion of ClearDrive Tech cultivated vital professional engineering competencies "
        "essential for industry leadership and advanced research:",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "• <b>Full-Stack Systems Thinking:</b> Understanding how low-level optical sensor physics, embedded Linux OS threading, neural network weight quantization, "
        "and client-side web browser rendering interlock within a production-grade automotive cockpit.<br/>"
        "• <b>Empathy for the End User:</b> Designing for the real-world commercial truck driver or daily commuter traversing dangerous mountain ghat roads, "
        "ensuring that alerts are intuitive, non-distracting, and operate reliably without cellular connectivity.<br/>"
        "• <b>Scientific Integrity & Candidness:</b> Thoroughly documenting failure modes, edge cases, and algorithmic limitations rather than claiming flawless "
        "performance, fostering true engineering credibility.",
        styles['BulletItem']
    ))
    f.append(Spacer(1, 15))
    f.append(create_callout_box(
        "Chapter 7 Metacognitive Takeaway",
        "Project-Based Learning transformed theoretical machine learning coursework into an authentic, rigorous, and deeply fulfilling engineering endeavor, "
        "equipping our team with the skills to conceive, design, implement, and operate complex intelligent systems.",
        styles
    ))
    f.append(PageBreak())

    return f
