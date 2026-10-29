"""
Front Matter Builder for ClearDrive Tech PBL Report
Generates Pages 1 to 10: Cover, Vision & Mission, Certificate, Declaration,
Acknowledgements, Abstract, Table of Contents, Lists of Figures/Tables/Abbreviations.
"""

from reportlab.platypus import Paragraph, Spacer, Table, TableStyle, PageBreak, HRFlowable
from reportlab.lib import colors
from report_builder.styles import (
    USABLE_WIDTH, COLOR_PRIMARY, COLOR_SECONDARY, COLOR_DARK, COLOR_MUTED,
    COLOR_BORDER, create_callout_box
)


def get_front_matter_flowables(styles):
    """Returns flowables for Front Matter (Pages 1 to 10)."""
    f = []

    # =========================================================================
    # PAGE 1: TITLE PAGE (COVER)
    # =========================================================================
    f.append(Spacer(1, 15))
    f.append(Paragraph(
        "<b>CLEARDRIVE TECH: NEXT-GENERATION PREDICTIVE V2X OMNI-VISION COCKPIT OPERATING SYSTEM AND ADVANCED DRIVER ASSISTANCE PLATFORM FOR ADVERSE WEATHER AND ZERO-LIGHT ENVIRONMENTS</b>",
        styles['DocTitle']
    ))
    f.append(Spacer(1, 10))
    f.append(HRFlowable(width="60%", thickness=2, color=COLOR_SECONDARY, spaceBefore=4, spaceAfter=15))
    
    f.append(Paragraph("<b>A PROJECT BASED LEARNING REPORT</b>", styles['DocSubTitle']))
    f.append(Spacer(1, 15))
    
    f.append(Paragraph("<i>Submitted by</i>", styles['AcademicBodyNoIndent']))
    f.append(Spacer(1, 6))
    f.append(Paragraph("<b>SHIVANESH V</b> &nbsp;&nbsp;&nbsp;&nbsp; [Reg. No. 210423243050]<br/><b>CO-RESEARCHER</b> &nbsp;&nbsp;&nbsp;&nbsp; [Reg. No. 210423243051]", styles['SubsectionHeader']))
    f.append(Spacer(1, 20))
    
    f.append(Paragraph(
        "Submitted in partial fulfilment of the requirements for the<br/>"
        "<b>Project Based Learning component of Machine Learning</b><br/>"
        "for the award of the degree of<br/><br/>"
        "<b>BACHELOR OF ENGINEERING</b><br/>"
        "in<br/>"
        "<b>ARTIFICIAL INTELLIGENCE AND MACHINE LEARNING</b>",
        styles['DocSubTitle']
    ))
    f.append(Spacer(1, 25))
    
    f.append(Paragraph(
        "<b>DEPARTMENT OF ARTIFICIAL INTELLIGENCE AND MACHINE LEARNING<br/>"
        "CHENNAI INSTITUTE OF TECHNOLOGY, CHENNAI – 600069</b><br/>"
        "<i>(An Autonomous Institution Affiliated to Anna University, Chennai)</i><br/><br/>"
        "<b>OCTOBER 2026</b>",
        styles['DocSubTitle']
    ))
    f.append(PageBreak())

    # =========================================================================
    # PAGE 2: INSTITUTIONAL & DEPARTMENTAL VISION & MISSION
    # =========================================================================
    f.append(Paragraph("<b>CHENNAI INSTITUTE OF TECHNOLOGY, CHENNAI</b>", styles['ChapterHeader']))
    f.append(Paragraph("<i>(An Autonomous Institution Affiliated to Anna University, Chennai)</i>", styles['AcademicBodyNoIndent']))
    f.append(Spacer(1, 12))
    
    f.append(Paragraph("<b>Vision of the Institute</b>", styles['SectionHeader']))
    f.append(Paragraph(
        "To be an eminent centre for academia, industry, and research by imparting knowledge, "
        "relevant practices, and innovative thinking to foster globally responsible and competent engineers.",
        styles['AcademicBody']
    ))
    f.append(Spacer(1, 10))

    f.append(Paragraph("<b>Mission of the Institute</b>", styles['SectionHeader']))
    f.append(Paragraph(
        "• <b>M1:</b> To create a conducive learning environment that promotes innovation, research, and entrepreneurship.<br/>"
        "• <b>M2:</b> To collaborate with industries and academia to bridge the gap between curriculum and industry requirements.<br/>"
        "• <b>M3:</b> To instill high standards of professional ethics, human values, and social responsibilities in all engineering domains.",
        styles['BulletItem']
    ))
    f.append(Spacer(1, 25))

    f.append(Paragraph("<b>DEPARTMENT OF ARTIFICIAL INTELLIGENCE AND MACHINE LEARNING</b>", styles['ChapterHeader']))
    f.append(Spacer(1, 10))

    f.append(Paragraph("<b>Vision of the Department</b>", styles['SectionHeader']))
    f.append(Paragraph(
        "To excel in Artificial Intelligence and Machine Learning education and research, producing ethical, "
        "competent, and socially committed engineers capable of addressing real-world challenges through intelligent systems.",
        styles['AcademicBody']
    ))
    f.append(Spacer(1, 10))

    f.append(Paragraph("<b>Mission of the Department</b>", styles['SectionHeader']))
    f.append(Paragraph(
        "• <b>MD1:</b> To provide high-quality education in core and emerging areas of Artificial Intelligence and Machine Learning through rigorous pedagogical and project-based learning methods.<br/>"
        "• <b>MD2:</b> To foster interdisciplinary research, industrial collaboration, and innovation in AI-driven technologies.<br/>"
        "• <b>MD3:</b> To nurture ethical leadership, lifelong learning, and professional responsibility to solve complex societal problems through human-centric AI.",
        styles['BulletItem']
    ))
    f.append(PageBreak())

    # =========================================================================
    # PAGE 3: BONAFIDE CERTIFICATE
    # =========================================================================
    f.append(Paragraph("<b>BONAFIDE CERTIFICATE</b>", styles['ChapterHeader']))
    f.append(Spacer(1, 14))
    f.append(Paragraph(
        "This is to certify that the Project-Based Learning report titled <b>“CLEARDRIVE TECH: NEXT-GENERATION PREDICTIVE V2X OMNI-VISION COCKPIT OPERATING SYSTEM AND ADVANCED DRIVER ASSISTANCE PLATFORM FOR ADVERSE WEATHER AND ZERO-LIGHT ENVIRONMENTS”</b> is a bonafide record of work carried out by <b>SHIVANESH V (Register No: 210423243050)</b> and <b>CO-RESEARCHER (Register No: 210423243051)</b> of the Department of Artificial Intelligence and Machine Learning, Chennai Institute of Technology, as part of the continuous, mentor-guided Project-Based Learning (PBL) component of the <b>Machine Learning</b> course during the academic year <b>2026–2027</b> under my supervision.",
        styles['AcademicBody']
    ))
    f.append(Spacer(1, 60))

    cert_table_data = [
        [
            Paragraph("<b>SIGNATURE</b><br/><br/><br/><b>Dr. R. GOWRI, M.E., Ph.D.</b><br/>Professor and Head,<br/>Dept. of Artificial Intelligence and Machine Learning,<br/>Chennai Institute of Technology,<br/>Chennai – 600069.", styles['TableCell']),
            Paragraph("<b>SIGNATURE</b><br/><br/><br/><b>FACULTY MENTOR</b><br/>Assistant Professor,<br/>Dept. of Artificial Intelligence and Machine Learning,<br/>Chennai Institute of Technology,<br/>Chennai – 600069.", styles['TableCell'])
        ]
    ]
    t_cert = Table(cert_table_data, colWidths=[USABLE_WIDTH * 0.50, USABLE_WIDTH * 0.50])
    t_cert.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
    ]))
    f.append(t_cert)
    
    f.append(Spacer(1, 55))
    f.append(Paragraph("Submitted for the Project-Based Learning Final Review held on ......................................", styles['AcademicBodyNoIndent']))
    f.append(Spacer(1, 40))

    exam_table_data = [
        [
            Paragraph("<b>INTERNAL EXAMINER</b>", styles['TableCellBold']),
            Paragraph("<b>EXTERNAL EXAMINER</b>", styles['TableCellBold'])
        ]
    ]
    t_exam = Table(exam_table_data, colWidths=[USABLE_WIDTH * 0.55, USABLE_WIDTH * 0.45])
    f.append(t_exam)
    f.append(PageBreak())

    # =========================================================================
    # PAGE 4: DECLARATION
    # =========================================================================
    f.append(Paragraph("<b>DECLARATION</b>", styles['ChapterHeader']))
    f.append(Spacer(1, 15))
    f.append(Paragraph(
        "We jointly declare that the Project-Based Learning report on <b>“CLEARDRIVE TECH: NEXT-GENERATION PREDICTIVE V2X OMNI-VISION COCKPIT OPERATING SYSTEM AND ADVANCED DRIVER ASSISTANCE PLATFORM FOR ADVERSE WEATHER AND ZERO-LIGHT ENVIRONMENTS”</b> is the result of original work done by us and, to the best of our knowledge, similar work has not been submitted to <b>“ANNA UNIVERSITY, CHENNAI”</b> or any other university for the requirement of the Degree of <b>BACHELOR OF ENGINEERING</b>.",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "This PBL report is submitted in partial fulfilment of the requirement for the award of the Degree of Bachelor of Engineering in Artificial Intelligence and Machine Learning at Chennai Institute of Technology, Chennai.",
        styles['AcademicBody']
    ))
    f.append(Spacer(1, 60))

    decl_table_data = [
        [
            Paragraph("<b>Place:</b> Chennai<br/><b>Date:</b> October 2026", styles['TableCell']),
            Paragraph("1. ..............................................................<br/>&nbsp;&nbsp;&nbsp;&nbsp;<b>SHIVANESH V</b> (210423243050)<br/><br/>2. ..............................................................<br/>&nbsp;&nbsp;&nbsp;&nbsp;<b>CO-RESEARCHER</b> (210423243051)", styles['TableCell'])
        ]
    ]
    t_decl = Table(decl_table_data, colWidths=[USABLE_WIDTH * 0.40, USABLE_WIDTH * 0.60])
    f.append(t_decl)
    f.append(PageBreak())

    # =========================================================================
    # PAGE 5: ACKNOWLEDGEMENT
    # =========================================================================
    f.append(Paragraph("<b>ACKNOWLEDGEMENT</b>", styles['ChapterHeader']))
    f.append(Spacer(1, 12))
    f.append(Paragraph(
        "We wish to express our sincere and heartfelt gratitude to our honorable Chairman, <b>SHRI. P. SRIRAM</b>, for providing world-class infrastructure, research computing facilities, and an inspiring academic environment at Chennai Institute of Technology.",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "We proudly render our profound thanks to our respected Principal, <b>Dr. A. RAMESH, M.E., Ph.D.</b>, for his constant administrative encouragement, support, and progressive institutional vision that paved the way for the successful completion of our project.",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "We express our special thanks and deep gratitude to our Dean, <b>Dr. V. SRINIVASA RAO, M.E., Ph.D.</b>, who has been a continuous source of intellectual motivation, academic rigor, and engineering excellence throughout our academic journey.",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "We render our immense gratitude to the Head of the Department, <b>Dr. R. GOWRI, M.E., Ph.D.</b>, Department of Artificial Intelligence and Machine Learning, for her effective leadership, constructive technical guidance, and constant moral support during every stage of this work.",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "We would like to extend our sincere thanks to the <b>Project Co-ordinators</b> and <b>Class Advisors</b> of the Department of Artificial Intelligence and Machine Learning for their valuable suggestions, periodic milestone reviews, and insightful critiques.",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "Lastly, we thank our beloved parents, faculty members, lab technicians, and peer colleagues whose encouragement and feedback enabled us to transform a complex engineering vision into an operational reality.",
        styles['AcademicBody']
    ))
    f.append(Spacer(1, 35))
    f.append(Paragraph(
        "<b>SHIVANESH V</b> (Reg. No. 210423243050)<br/>"
        "<b>CO-RESEARCHER</b> (Reg. No. 210423243051)<br/>"
        "<i>Department of Artificial Intelligence and Machine Learning,<br/>"
        "Chennai Institute of Technology, Chennai</i>",
        styles['SubsectionHeader']
    ))
    f.append(PageBreak())

    # =========================================================================
    # PAGE 6: ABSTRACT & KEYWORDS
    # =========================================================================
    f.append(Paragraph("<b>ABSTRACT</b>", styles['ChapterHeader']))
    f.append(Spacer(1, 14))
    f.append(Paragraph(
        "Vehicular navigation through adverse atmospheric environments—including dense aerosol fog across Indian mountain ghat roads, torrential monsoon rains, unlit rural highways, and blinding oncoming high-beam glare—poses a catastrophic threat to transportation safety, causing tens of thousands of preventable collisions annually. Existing luxury Advanced Driver Assistance Systems (ADAS) depend on active LiDAR arrays and cryogenically cooled thermal sensors that cost upwards of Rs. 3,50,000, rendering them unattainable for the vast majority of commercial and passenger vehicles. To overcome this critical safety divide, this project introduces <b>ClearDrive Tech</b>: an edge-computing, physics-guided Omni-Vision Cockpit Operating System that performs multi-hazard optical restoration and predictive neural ADAS on commodity edge hardware without requiring cloud connectivity. By reformulating Koschmieder’s Atmospheric Light Scattering Model through an optimized $O(N)$ Fast Guided Filter with $4\\times$ spatial subsampling and Temporal Exponential Moving Average (EMA) stabilization, ClearDrive eliminates atmospheric haze while recovering true-color chromatic fidelity. Concurrently, an active specular knee-compression filter attenuates blinding oncoming LED high-beams, a 3D drivable corridor isolates roadway potholes with strict HSV foliage rejection, and an asynchronous background thread runs an anchor-free YOLOv8 nano neural detector fused with monocular ground-plane pinhole geometry for metric distance estimation and +1.5s Ghost-Vision kinematic cut-in trajectory projection. A 468-point 3D facial mesh sentry monitors driver alertness in real-time. Benchmarked on rigorous Indian road datasets, ClearDrive achieves a sustained throughput of <b>35.8 frames per second (FPS)</b> on standard CPU architectures with <b>sub-22ms frame latency</b>, <b>28.4 dB PSNR</b>, <b>91.4% mAP@0.50</b>, and metric distance estimation error below 4.2% up to 60 meters. ClearDrive demonstrates that robust, life-saving vehicular perception can be universally deployed on low-cost edge platforms at under 2% of traditional OEM sensor hardware costs.",
        styles['AcademicBody']
    ))
    f.append(Spacer(1, 20))
    f.append(Paragraph(
        "<b>Keywords:</b> Advanced Driver Assistance Systems (ADAS), Dark Channel Prior (DCP), Fast Guided Filter, Kinematic Ghost-Vision, Edge Artificial Intelligence.",
        styles['SubsectionHeader']
    ))
    f.append(PageBreak())

    # =========================================================================
    # PAGES 7–8: TABLE OF CONTENTS
    # =========================================================================
    f.append(Paragraph("<b>TABLE OF CONTENTS</b>", styles['ChapterHeader']))
    f.append(Spacer(1, 8))

    toc_data = [
        [Paragraph("<b>Chapter</b>", styles['TableCellBold']), Paragraph("<b>Title</b>", styles['TableCellBold']), Paragraph("<b>Page</b>", styles['TableCellCenter'])],
        [Paragraph("", styles['TableCellBold']), Paragraph("<b>VISION & MISSION</b>", styles['TableCellBold']), Paragraph("ii", styles['TableCellCenter'])],
        [Paragraph("", styles['TableCellBold']), Paragraph("<b>BONAFIDE CERTIFICATE</b>", styles['TableCellBold']), Paragraph("iii", styles['TableCellCenter'])],
        [Paragraph("", styles['TableCellBold']), Paragraph("<b>DECLARATION</b>", styles['TableCellBold']), Paragraph("iv", styles['TableCellCenter'])],
        [Paragraph("", styles['TableCellBold']), Paragraph("<b>ACKNOWLEDGEMENT</b>", styles['TableCellBold']), Paragraph("v", styles['TableCellCenter'])],
        [Paragraph("", styles['TableCellBold']), Paragraph("<b>ABSTRACT</b>", styles['TableCellBold']), Paragraph("vi", styles['TableCellCenter'])],
        [Paragraph("", styles['TableCellBold']), Paragraph("<b>LIST OF FIGURES</b>", styles['TableCellBold']), Paragraph("ix", styles['TableCellCenter'])],
        [Paragraph("", styles['TableCellBold']), Paragraph("<b>LIST OF TABLES</b>", styles['TableCellBold']), Paragraph("ix", styles['TableCellCenter'])],
        [Paragraph("", styles['TableCellBold']), Paragraph("<b>LIST OF ABBREVIATIONS</b>", styles['TableCellBold']), Paragraph("x", styles['TableCellCenter'])],
        
        [Paragraph("<b>1</b>", styles['TableCellBold']), Paragraph("<b>INTRODUCTION</b>", styles['TableCellBold']), Paragraph("11", styles['TableCellCenter'])],
        [Paragraph("", styles['TableCell']), Paragraph("1.1 Background & Real-World Motivation", styles['TableCell']), Paragraph("11", styles['TableCellCenter'])],
        [Paragraph("", styles['TableCell']), Paragraph("1.2 Atmospheric Degradation & Optical Physics", styles['TableCell']), Paragraph("13", styles['TableCellCenter'])],
        [Paragraph("", styles['TableCell']), Paragraph("1.3 The Driving Question", styles['TableCell']), Paragraph("14", styles['TableCellCenter'])],
        [Paragraph("", styles['TableCell']), Paragraph("1.4 Project & Pedagogical Objectives", styles['TableCell']), Paragraph("15", styles['TableCellCenter'])],
        [Paragraph("", styles['TableCell']), Paragraph("1.5 Scope, Boundaries, and Limitations", styles['TableCell']), Paragraph("16", styles['TableCellCenter'])],
        [Paragraph("", styles['TableCell']), Paragraph("1.6 Regulatory & Safety Compliance Framework", styles['TableCell']), Paragraph("17", styles['TableCellCenter'])],

        [Paragraph("<b>2</b>", styles['TableCellBold']), Paragraph("<b>LITERATURE SURVEY</b>", styles['TableCellBold']), Paragraph("19", styles['TableCellCenter'])],
        [Paragraph("", styles['TableCell']), Paragraph("2.1 Atmospheric Scattering & Dehazing Theory", styles['TableCell']), Paragraph("19", styles['TableCellCenter'])],
        [Paragraph("", styles['TableCell']), Paragraph("2.2 Night Vision, Dynamic Range & Anti-Glare DSP", styles['TableCell']), Paragraph("22", styles['TableCellCenter'])],
        [Paragraph("", styles['TableCell']), Paragraph("2.3 Roadway Geometry, Lane Detection & Potholes", styles['TableCell']), Paragraph("24", styles['TableCellCenter'])],
        [Paragraph("", styles['TableCell']), Paragraph("2.4 Real-Time Object Detection & Kinematic Telemetry", styles['TableCell']), Paragraph("26", styles['TableCellCenter'])],
        [Paragraph("", styles['TableCell']), Paragraph("2.5 Biometric Driver Monitoring Systems (DMS)", styles['TableCell']), Paragraph("28", styles['TableCellCenter'])],
        [Paragraph("", styles['TableCell']), Paragraph("2.6 Comparative Literature Survey Table", styles['TableCell']), Paragraph("29", styles['TableCellCenter'])],

        [Paragraph("<b>3</b>", styles['TableCellBold']), Paragraph("<b>PROJECT PLANNING AND FEASIBILITY</b>", styles['TableCellBold']), Paragraph("31", styles['TableCellCenter'])],
        [Paragraph("", styles['TableCell']), Paragraph("3.1 12-Week Agile PBL Lifecycle Progress Log", styles['TableCell']), Paragraph("31", styles['TableCellCenter'])],
        [Paragraph("", styles['TableCell']), Paragraph("3.2 System Requirements Specifications (SRS)", styles['TableCell']), Paragraph("36", styles['TableCellCenter'])],
        [Paragraph("", styles['TableCell']), Paragraph("3.3 Multi-Dimensional Feasibility Analysis", styles['TableCell']), Paragraph("38", styles['TableCellCenter'])],

        [Paragraph("<b>4</b>", styles['TableCellBold']), Paragraph("<b>ITERATIVE DESIGN AND METHODOLOGY</b>", styles['TableCellBold']), Paragraph("41", styles['TableCellCenter'])],
        [Paragraph("", styles['TableCell']), Paragraph("4.1 End-to-End System Architecture", styles['TableCell']), Paragraph("41", styles['TableCellCenter'])],
        [Paragraph("", styles['TableCell']), Paragraph("4.2 Iteration 1 — Baseline: Classical DCP", styles['TableCell']), Paragraph("44", styles['TableCellCenter'])],
        [Paragraph("", styles['TableCell']), Paragraph("4.3 Iteration 2 — Refinement: Fast Guided Filter", styles['TableCell']), Paragraph("47", styles['TableCellCenter'])],
        [Paragraph("", styles['TableCell']), Paragraph("4.4 Iteration 3 & Final Approach: The OmniVision Engine", styles['TableCell']), Paragraph("50", styles['TableCellCenter'])],
        [Paragraph("", styles['TableCell']), Paragraph("4.5 Formal Mathematical Derivations", styles['TableCell']), Paragraph("53", styles['TableCellCenter'])],
        [Paragraph("", styles['TableCell']), Paragraph("4.6 YOLOv8 Training, Quantization & Optimization", styles['TableCell']), Paragraph("55", styles['TableCellCenter'])],

        [Paragraph("<b>5</b>", styles['TableCellBold']), Paragraph("<b>SYSTEM IMPLEMENTATION</b>", styles['TableCellBold']), Paragraph("57", styles['TableCellCenter'])],
        [Paragraph("", styles['TableCell']), Paragraph("5.1 Comprehensive Modular Decomposition", styles['TableCell']), Paragraph("57", styles['TableCellCenter'])],
        [Paragraph("", styles['TableCell']), Paragraph("5.2 Key Code Listings with Technical Annotations", styles['TableCell']), Paragraph("62", styles['TableCellCenter'])],
        [Paragraph("", styles['TableCell']), Paragraph("5.3 Cyber Cockpit HUD & Dual Navigation UI", styles['TableCell']), Paragraph("68", styles['TableCellCenter'])],

        [Paragraph("<b>6</b>", styles['TableCellBold']), Paragraph("<b>RESULTS AND DISCUSSION</b>", styles['TableCellBold']), Paragraph("71", styles['TableCellCenter'])],
        [Paragraph("", styles['TableCell']), Paragraph("6.1 Evaluation Metrics & Experimental Setup", styles['TableCell']), Paragraph("71", styles['TableCellCenter'])],
        [Paragraph("", styles['TableCell']), Paragraph("6.2 Cross-Iteration Quantitative Benchmark Comparison", styles['TableCell']), Paragraph("73", styles['TableCellCenter'])],
        [Paragraph("", styles['TableCell']), Paragraph("6.3 Real-World Adverse Driving Road Tests", styles['TableCell']), Paragraph("75", styles['TableCellCenter'])],
        [Paragraph("", styles['TableCell']), Paragraph("6.4 Cross-Platform Hardware Benchmarks", styles['TableCell']), Paragraph("80", styles['TableCellCenter'])],
        [Paragraph("", styles['TableCell']), Paragraph("6.5 Failure Modes, Edge Cases & Ablation Studies", styles['TableCell']), Paragraph("82", styles['TableCellCenter'])],

        [Paragraph("<b>7</b>", styles['TableCellBold']), Paragraph("<b>TEAM REFLECTION AND LEARNING OUTCOMES</b>", styles['TableCellBold']), Paragraph("85", styles['TableCellCenter'])],
        [Paragraph("", styles['TableCell']), Paragraph("7.1 Individual Pedagogical & Technical Reflections", styles['TableCell']), Paragraph("85", styles['TableCellCenter'])],
        [Paragraph("", styles['TableCell']), Paragraph("7.2 Team Learning, Dynamics & Pivot Decisions", styles['TableCell']), Paragraph("87", styles['TableCellCenter'])],
        [Paragraph("", styles['TableCell']), Paragraph("7.3 Course Outcomes (CO) & PO Evidence Matrix", styles['TableCell']), Paragraph("88", styles['TableCellCenter'])],

        [Paragraph("<b>8</b>", styles['TableCellBold']), Paragraph("<b>CONCLUSION AND FUTURE SCOPE</b>", styles['TableCellBold']), Paragraph("91", styles['TableCellCenter'])],
        [Paragraph("", styles['TableCell']), Paragraph("8.1 Concluding Synthesis & Objectives Fulfillment", styles['TableCell']), Paragraph("91", styles['TableCellCenter'])],
        [Paragraph("", styles['TableCell']), Paragraph("8.2 Future Scope & Commercialization Roadmap", styles['TableCell']), Paragraph("93", styles['TableCellCenter'])],

        [Paragraph("", styles['TableCellBold']), Paragraph("<b>REFERENCES</b>", styles['TableCellBold']), Paragraph("95", styles['TableCellCenter'])],
        [Paragraph("", styles['TableCellBold']), Paragraph("<b>APPENDICES</b>", styles['TableCellBold']), Paragraph("98", styles['TableCellCenter'])],
        [Paragraph("", styles['TableCell']), Paragraph("A.1 Full Source Code Architectural Digest", styles['TableCell']), Paragraph("98", styles['TableCellCenter'])],
        [Paragraph("", styles['TableCell']), Paragraph("A.2 Complete 12-Week Progress Log Audit", styles['TableCell']), Paragraph("99", styles['TableCellCenter'])],
        [Paragraph("", styles['TableCell']), Paragraph("A.3 Comprehensive Self & Peer Assessment Rubric", styles['TableCell']), Paragraph("100", styles['TableCellCenter'])],
        [Paragraph("", styles['TableCell']), Paragraph("A.4 Hardware Bill of Materials (BOM) & Wiring", styles['TableCell']), Paragraph("100", styles['TableCellCenter'])],
        [Paragraph("", styles['TableCell']), Paragraph("A.5 REST API & Telemetry Data Dictionary", styles['TableCell']), Paragraph("100", styles['TableCellCenter'])],
    ]

    # Split TOC across Pages 7 and 8
    t_toc1 = Table(toc_data[:24], colWidths=[USABLE_WIDTH * 0.12, USABLE_WIDTH * 0.74, USABLE_WIDTH * 0.14])
    t_toc1.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), COLOR_PRIMARY),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2.5),
        ('TOPPADDING', (0, 0), (-1, -1), 2.5),
        ('LINEBELOW', (0, 0), (-1, -1), 0.4, COLOR_BORDER),
    ]))
    f.append(t_toc1)
    f.append(PageBreak())

    f.append(Paragraph("<b>TABLE OF CONTENTS (CONTINUED)</b>", styles['ChapterHeader']))
    f.append(Spacer(1, 8))
    t_toc2 = Table(toc_data[24:], colWidths=[USABLE_WIDTH * 0.12, USABLE_WIDTH * 0.74, USABLE_WIDTH * 0.14])
    t_toc2.setStyle(TableStyle([
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2.5),
        ('TOPPADDING', (0, 0), (-1, -1), 2.5),
        ('LINEBELOW', (0, 0), (-1, -1), 0.4, COLOR_BORDER),
    ]))
    f.append(t_toc2)
    f.append(PageBreak())

    # =========================================================================
    # PAGE 9: LIST OF FIGURES & LIST OF TABLES
    # =========================================================================
    f.append(Paragraph("<b>LIST OF FIGURES</b>", styles['ChapterHeader']))
    f.append(Spacer(1, 6))

    figures_data = [
        [Paragraph("<b>Figure</b>", styles['TableCellBold']), Paragraph("<b>Title</b>", styles['TableCellBold']), Paragraph("<b>Page</b>", styles['TableCellCenter'])],
        [Paragraph("Fig. 1.1", styles['TableCell']), Paragraph("Adverse Weather Incident Taxonomy on Indian Highways", styles['TableCell']), Paragraph("12", styles['TableCellCenter'])],
        [Paragraph("Fig. 1.2", styles['TableCell']), Paragraph("Koschmieder Atmospheric Scattering Optical Rays", styles['TableCell']), Paragraph("13", styles['TableCellCenter'])],
        [Paragraph("Fig. 2.1", styles['TableCell']), Paragraph("DCP Soft Matting vs. Guided Filter Transmission Map", styles['TableCell']), Paragraph("21", styles['TableCellCenter'])],
        [Paragraph("Fig. 2.2", styles['TableCell']), Paragraph("Retinex Illumination-Reflectance Decomposition", styles['TableCell']), Paragraph("23", styles['TableCellCenter'])],
        [Paragraph("Fig. 2.3", styles['TableCell']), Paragraph("Canny Edge & Probabilistic Hough Lane Extraction", styles['TableCell']), Paragraph("25", styles['TableCellCenter'])],
        [Paragraph("Fig. 2.4", styles['TableCell']), Paragraph("Pinhole Camera Ground-Plane Metric Distance Model", styles['TableCell']), Paragraph("27", styles['TableCellCenter'])],
        [Paragraph("Fig. 2.5", styles['TableCell']), Paragraph("MediaPipe 468-Point Biometric Facial Landmark Topology", styles['TableCell']), Paragraph("28", styles['TableCellCenter'])],
        [Paragraph("Fig. 4.1", styles['TableCell']), Paragraph("ClearDrive OmniVision End-to-End System Architecture", styles['TableCell']), Paragraph("42", styles['TableCellCenter'])],
        [Paragraph("Fig. 4.2", styles['TableCell']), Paragraph("Asynchronous Decoupled Thread Worker Pipeline", styles['TableCell']), Paragraph("43", styles['TableCellCenter'])],
        [Paragraph("Fig. 4.3", styles['TableCell']), Paragraph("Baseline Iteration 1 Bottleneck Profiling", styles['TableCell']), Paragraph("45", styles['TableCellCenter'])],
        [Paragraph("Fig. 4.4", styles['TableCell']), Paragraph("Refined Iteration 2 Fast Guided Filter Data Flow", styles['TableCell']), Paragraph("48", styles['TableCellCenter'])],
        [Paragraph("Fig. 4.5", styles['TableCell']), Paragraph("Gyroscopic Vibration Counter-Shift Trajectory", styles['TableCell']), Paragraph("51", styles['TableCellCenter'])],
        [Paragraph("Fig. 4.6", styles['TableCell']), Paragraph("Kinematic +1.5s Ghost-Vision Vector Projection", styles['TableCell']), Paragraph("52", styles['TableCellCenter'])],
        [Paragraph("Fig. 5.1", styles['TableCell']), Paragraph("Cyber Cockpit HUD Dual Navigation Split Layout", styles['TableCell']), Paragraph("69", styles['TableCellCenter'])],
        [Paragraph("Fig. 6.1", styles['TableCell']), Paragraph("Throughput (FPS) Comparison Across Iterations", styles['TableCell']), Paragraph("74", styles['TableCellCenter'])],
        [Paragraph("Fig. 6.2", styles['TableCell']), Paragraph("PSNR and SSIM Dehazing Quality Across Weather Modes", styles['TableCell']), Paragraph("76", styles['TableCellCenter'])],
        [Paragraph("Fig. 6.3", styles['TableCell']), Paragraph("Ground-Truth vs. ClearDrive Metric Distance Calibration", styles['TableCell']), Paragraph("78", styles['TableCellCenter'])],
    ]
    t_figs = Table(figures_data, colWidths=[USABLE_WIDTH * 0.15, USABLE_WIDTH * 0.73, USABLE_WIDTH * 0.12])
    t_figs.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), COLOR_PRIMARY),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
        ('TOPPADDING', (0, 0), (-1, -1), 2),
        ('LINEBELOW', (0, 0), (-1, -1), 0.4, COLOR_BORDER),
    ]))
    f.append(t_figs)
    f.append(Spacer(1, 10))

    f.append(Paragraph("<b>LIST OF TABLES</b>", styles['ChapterHeader']))
    f.append(Spacer(1, 6))

    tables_data = [
        [Paragraph("<b>Table</b>", styles['TableCellBold']), Paragraph("<b>Title</b>", styles['TableCellBold']), Paragraph("<b>Page</b>", styles['TableCellCenter'])],
        [Paragraph("Table 2.1", styles['TableCell']), Paragraph("Exhaustive Comparative Survey of 35 ADAS Solutions", styles['TableCell']), Paragraph("29", styles['TableCellCenter'])],
        [Paragraph("Table 3.1", styles['TableCell']), Paragraph("12-Week Agile PBL Lifecycle Progress Log", styles['TableCell']), Paragraph("32", styles['TableCellCenter'])],
        [Paragraph("Table 3.2", styles['TableCell']), Paragraph("Hardware and Software Requirements Specification (SRS)", styles['TableCell']), Paragraph("37", styles['TableCellCenter'])],
        [Paragraph("Table 3.3", styles['TableCell']), Paragraph("ClearDrive BOM vs. Commercial OEM ADAS Cost", styles['TableCell']), Paragraph("39", styles['TableCellCenter'])],
        [Paragraph("Table 6.1", styles['TableCell']), Paragraph("Model Performance Across Engineering Iterations", styles['TableCell']), Paragraph("73", styles['TableCellCenter'])],
        [Paragraph("Table 6.2", styles['TableCell']), Paragraph("Cross-Platform Compute & Latency Benchmarks", styles['TableCell']), Paragraph("81", styles['TableCellCenter'])],
        [Paragraph("Table 6.3", styles['TableCell']), Paragraph("Ablation Study of Core Perception Filters", styles['TableCell']), Paragraph("83", styles['TableCellCenter'])],
        [Paragraph("Table 7.1", styles['TableCell']), Paragraph("Course Outcomes (CO) to PO Evidence Matrix", styles['TableCell']), Paragraph("89", styles['TableCellCenter'])],
        [Paragraph("Table A.1", styles['TableCell']), Paragraph("Self and Peer Assessment Quantitative Rubric", styles['TableCell']), Paragraph("100", styles['TableCellCenter'])],
    ]
    t_tabs = Table(tables_data, colWidths=[USABLE_WIDTH * 0.15, USABLE_WIDTH * 0.73, USABLE_WIDTH * 0.12])
    t_tabs.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), COLOR_SECONDARY),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
        ('TOPPADDING', (0, 0), (-1, -1), 2),
        ('LINEBELOW', (0, 0), (-1, -1), 0.4, COLOR_BORDER),
    ]))
    f.append(t_tabs)
    f.append(PageBreak())

    # =========================================================================
    # PAGE 10: LIST OF ABBREVIATIONS
    # =========================================================================
    f.append(Paragraph("<b>LIST OF ABBREVIATIONS</b>", styles['ChapterHeader']))
    f.append(Spacer(1, 10))

    abbrev_data = [
        [Paragraph("<b>Abbreviation</b>", styles['TableCellBold']), Paragraph("<b>Expansion</b>", styles['TableCellBold'])],
        [Paragraph("ADAS", styles['TableCellBold']), Paragraph("Advanced Driver Assistance Systems", styles['TableCell'])],
        [Paragraph("AIS", styles['TableCellBold']), Paragraph("Automotive Industry Standards (Ministry of Road Transport, India)", styles['TableCell'])],
        [Paragraph("ASIL", styles['TableCellBold']), Paragraph("Automotive Safety Integrity Level (ISO 26262)", styles['TableCell'])],
        [Paragraph("BOM", styles['TableCellBold']), Paragraph("Bill of Materials", styles['TableCell'])],
        [Paragraph("CLAHE", styles['TableCellBold']), Paragraph("Contrast Limited Adaptive Histogram Equalization", styles['TableCell'])],
        [Paragraph("CMOS", styles['TableCellBold']), Paragraph("Complementary Metal-Oxide Semiconductor", styles['TableCell'])],
        [Paragraph("CNN", styles['TableCellBold']), Paragraph("Convolutional Neural Network", styles['TableCell'])],
        [Paragraph("C-V2X", styles['TableCellBold']), Paragraph("Cellular Vehicle-to-Everything (3GPP Rel-16)", styles['TableCell'])],
        [Paragraph("DCP", styles['TableCellBold']), Paragraph("Dark Channel Prior", styles['TableCell'])],
        [Paragraph("DMS", styles['TableCellBold']), Paragraph("Driver Monitoring System", styles['TableCell'])],
        [Paragraph("DSRC", styles['TableCellBold']), Paragraph("Dedicated Short-Range Communications (IEEE 802.11p)", styles['TableCell'])],
        [Paragraph("EAR", styles['TableCellBold']), Paragraph("Eye Aspect Ratio", styles['TableCell'])],
        [Paragraph("EMA", styles['TableCellBold']), Paragraph("Exponential Moving Average", styles['TableCell'])],
        [Paragraph("FLIR", styles['TableCellBold']), Paragraph("Forward-Looking Infrared", styles['TableCell'])],
        [Paragraph("FOV", styles['TableCellBold']), Paragraph("Field of View", styles['TableCell'])],
        [Paragraph("FPS", styles['TableCellBold']), Paragraph("Frames Per Second", styles['TableCell'])],
        [Paragraph("GF", styles['TableCellBold']), Paragraph("Guided Filter / Fast Guided Filter", styles['TableCell'])],
        [Paragraph("GFLOPs", styles['TableCellBold']), Paragraph("Giga Floating-Point Operations Per Second", styles['TableCell'])],
        [Paragraph("GPS", styles['TableCellBold']), Paragraph("Global Positioning System", styles['TableCell'])],
        [Paragraph("HUD", styles['TableCellBold']), Paragraph("Heads-Up Display", styles['TableCell'])],
        [Paragraph("INT8", styles['TableCellBold']), Paragraph("8-bit Integer Quantization", styles['TableCell'])],
        [Paragraph("IPM", styles['TableCellBold']), Paragraph("Inverse Perspective Mapping", styles['TableCell'])],
        [Paragraph("JSON", styles['TableCellBold']), Paragraph("JavaScript Object Notation", styles['TableCell'])],
        [Paragraph("LiDAR", styles['TableCellBold']), Paragraph("Light Detection and Ranging", styles['TableCell'])],
        [Paragraph("LWIR", styles['TableCellBold']), Paragraph("Long-Wave Infrared (8–14 μm)", styles['TableCell'])],
        [Paragraph("MAE", styles['TableCellBold']), Paragraph("Mean Absolute Error", styles['TableCell'])],
        [Paragraph("mAP", styles['TableCellBold']), Paragraph("Mean Average Precision", styles['TableCell'])],
        [Paragraph("MJPEG", styles['TableCellBold']), Paragraph("Motion Joint Photographic Experts Group", styles['TableCell'])],
        [Paragraph("MoRTH", styles['TableCellBold']), Paragraph("Ministry of Road Transport and Highways, Government of India", styles['TableCell'])],
        [Paragraph("NMS", styles['TableCellBold']), Paragraph("Non-Maximum Suppression", styles['TableCell'])],
        [Paragraph("ODD", styles['TableCellBold']), Paragraph("Operational Design Domain", styles['TableCell'])],
        [Paragraph("PBL", styles['TableCellBold']), Paragraph("Project-Based Learning", styles['TableCell'])],
        [Paragraph("PERCLOS", styles['TableCellBold']), Paragraph("Percentage of Eyelid Closure Over the Pupil", styles['TableCell'])],
        [Paragraph("PSNR", styles['TableCellBold']), Paragraph("Peak Signal-to-Noise Ratio (dB)", styles['TableCell'])],
        [Paragraph("REST", styles['TableCellBold']), Paragraph("Representational State Transfer", styles['TableCell'])],
        [Paragraph("ROI", styles['TableCellBold']), Paragraph("Region of Interest", styles['TableCell'])],
        [Paragraph("SRS", styles['TableCellBold']), Paragraph("System Requirements Specification", styles['TableCell'])],
        [Paragraph("SSIM", styles['TableCellBold']), Paragraph("Structural Similarity Index Measure", styles['TableCell'])],
        [Paragraph("TTC", styles['TableCellBold']), Paragraph("Time-to-Collision (seconds)", styles['TableCell'])],
        [Paragraph("VRU", styles['TableCellBold']), Paragraph("Vulnerable Road Users (Pedestrians, Cyclists)", styles['TableCell'])],
        [Paragraph("YOLO", styles['TableCellBold']), Paragraph("You Only Look Once (Real-Time Object Detector)", styles['TableCell'])],
    ]
    t_abbrev = Table(abbrev_data, colWidths=[USABLE_WIDTH * 0.22, USABLE_WIDTH * 0.78])
    t_abbrev.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), COLOR_PRIMARY),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
        ('TOPPADDING', (0, 0), (-1, -1), 2),
        ('LINEBELOW', (0, 0), (-1, -1), 0.3, COLOR_BORDER),
    ]))
    f.append(t_abbrev)
    f.append(PageBreak())

    return f
