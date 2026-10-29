"""
Front Matter: Title, Bonafide, Vision/Mission, TOC, LOF, LOT, and Abbreviations
Pages 1 to 5 (Exactly 5 Pages)
ClearDrive AI: 55-Page Project-Based Learning Report
"""

from reportlab.platypus import Paragraph, Spacer, Table, TableStyle, PageBreak, HRFlowable
from reportlab.lib import colors
from report_builder_55.styles import (
    USABLE_WIDTH, COLOR_PRIMARY, COLOR_SECONDARY, COLOR_BORDER
)


def get_front_matter_flowables(styles):
    """Returns flowables for Front Matter (Pages 1 to 5 - Exactly 5 Pages)."""
    f = []

    # =========================================================================
    # PAGE 1: TITLE PAGE & OFFICIAL BONAFIDE CERTIFICATE
    # =========================================================================
    f.append(Spacer(1, 4))
    f.append(Paragraph("<b>CHENNAI INSTITUTE OF TECHNOLOGY, CHENNAI - 600069</b>", styles['CoverInstitution']))
    f.append(Paragraph("<i>(An Autonomous Institution Affiliated to Anna University, Chennai)</i>", styles['CoverBody']))
    f.append(Paragraph("<b>DEPARTMENT OF ARTIFICIAL INTELLIGENCE AND MACHINE LEARNING</b>", styles['CoverDept']))
    f.append(HRFlowable(width="90%", thickness=1.0, color=COLOR_PRIMARY, spaceBefore=3, spaceAfter=8))

    f.append(Paragraph(
        "<b>CLEARDRIVE AI: REAL-TIME ADAS AND VISION RESTORATION FOR ADVERSE DRIVING CONDITIONS</b>",
        styles['DocTitle']
    ))
    f.append(Paragraph("<b>A PROJECT BASED LEARNING REPORT</b>", styles['DocSubTitle']))
    f.append(Spacer(1, 4))

    f.append(Paragraph("<i>Submitted by</i>", styles['CoverBody']))
    f.append(Paragraph("<b>SHIVANESH V</b> [Reg. No. 210425148109] &nbsp;&nbsp;&nbsp;&nbsp; <b>VISHNU PRASATH S</b> [Reg. No. 210425148134]", styles['SubsectionHeader']))
    f.append(Spacer(1, 4))

    f.append(Paragraph(
        "Submitted in partial fulfilment of the requirements for the<br/>"
        "<b>Project Based Learning component of Machine Learning</b><br/>"
        "for the award of the degree of <b>BACHELOR OF ENGINEERING</b> in<br/>"
        "<b>ARTIFICIAL INTELLIGENCE AND MACHINE LEARNING</b> - <b>OCTOBER 2026</b>",
        styles['CoverBody']
    ))
    f.append(Spacer(1, 6))
    f.append(HRFlowable(width="100%", thickness=0.8, color=COLOR_SECONDARY, spaceBefore=2, spaceAfter=8))

    # Official Bonafide Certificate Section
    f.append(Paragraph("<b>BONAFIDE CERTIFICATE</b>", styles['ChapterHeader']))
    f.append(Spacer(1, 3))
    f.append(Paragraph(
        "This is to certify that the Project-Based Learning report titled <b>&quot;CLEARDRIVE AI: REAL-TIME ADAS AND VISION RESTORATION FOR ADVERSE DRIVING CONDITIONS&quot;</b> "
        "is a bonafide record of work carried out by <b>SHIVANESH V (Reg. No: 210425148109)</b> and <b>VISHNU PRASATH S (Reg. No: 210425148134)</b> of the Department of "
        "Artificial Intelligence and Machine Learning, Chennai Institute of Technology, as part of the continuous, mentor-guided Project-Based Learning (PBL) component "
        "of the <b>Machine Learning</b> course during the academic year <b>2026-2027</b> under my supervision.",
        styles['AcademicBodyNoIndent']
    ))
    f.append(Spacer(1, 24))

    cert_table_data = [
        [
            Paragraph("<b>SIGNATURE</b><br/><br/><br/><b>Dr. R. GOWRI, M.E., Ph.D.</b><br/>Professor and Head,<br/>Dept. of Artificial Intelligence & Machine Learning,<br/>Chennai Institute of Technology,<br/>Chennai - 600069.", styles['TableCell']),
            Paragraph("<b>SIGNATURE</b><br/><br/><br/><b>FACULTY MENTOR</b><br/>Assistant Professor,<br/>Dept. of Artificial Intelligence & Machine Learning,<br/>Chennai Institute of Technology,<br/>Chennai - 600069.", styles['TableCell'])
        ]
    ]
    t_cert = Table(cert_table_data, colWidths=[USABLE_WIDTH * 0.52, USABLE_WIDTH * 0.48])
    t_cert.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
    ]))
    f.append(t_cert)

    f.append(Spacer(1, 20))
    f.append(Paragraph("Submitted for the Project-Based Learning Final Review held on ......................................", styles['AcademicBodyNoIndent']))
    f.append(Spacer(1, 16))

    exam_table_data = [
        [
            Paragraph("<b>INTERNAL EXAMINER</b>", styles['TableCellBold']),
            Paragraph("<b>EXTERNAL EXAMINER</b>", styles['TableCellBold'])
        ]
    ]
    t_exam = Table(exam_table_data, colWidths=[USABLE_WIDTH * 0.52, USABLE_WIDTH * 0.48])
    t_exam.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
    ]))
    f.append(t_exam)

    f.append(PageBreak())

    # =========================================================================
    # PAGE 2: INSTITUTIONAL & DEPARTMENTAL VISION & MISSION
    # =========================================================================
    f.append(Spacer(1, 8))
    f.append(Paragraph("<b>CHENNAI INSTITUTE OF TECHNOLOGY, CHENNAI</b>", styles['ChapterHeader']))
    f.append(Paragraph("<i>(An Autonomous Institution Affiliated to Anna University, Chennai)</i>", styles['AcademicBodyNoIndent']))
    f.append(Spacer(1, 10))

    f.append(Paragraph("<b>Vision of the Institute</b>", styles['SectionHeader']))
    f.append(Paragraph(
        "To be an eminent centre for academia, industry, and research by imparting knowledge, "
        "relevant practices, and innovative thinking to foster globally responsible and competent engineers.",
        styles['AcademicBody']
    ))
    f.append(Spacer(1, 8))

    f.append(Paragraph("<b>Mission of the Institute</b>", styles['SectionHeader']))
    f.append(Paragraph(
        "• <b>M1:</b> To create a conducive learning environment that promotes innovation, research, and entrepreneurship.<br/>"
        "• <b>M2:</b> To collaborate with industries and academia to bridge the gap between curriculum and industry requirements.<br/>"
        "• <b>M3:</b> To instill high standards of professional ethics, human values, and social responsibilities in all engineering domains.<br/>"
        "• <b>M4:</b> To contribute towards the research ecosystem by providing a suitable infrastructure and incubation environment.",
        styles['BulletItem']
    ))
    f.append(Spacer(1, 10))
    f.append(HRFlowable(width="100%", thickness=0.8, color=COLOR_SECONDARY, spaceBefore=2, spaceAfter=8))

    f.append(Paragraph("<b>DEPARTMENT OF ARTIFICIAL INTELLIGENCE AND MACHINE LEARNING</b>", styles['ChapterHeader']))
    f.append(Spacer(1, 5))

    f.append(Paragraph("<b>Vision of the Department</b>", styles['SectionHeader']))
    f.append(Paragraph(
        "“Developing skilled AI and ML professionals empowered through research and innovation to address global challenges and to enhance societal well-being.”<br/>"
        "To excel in Artificial Intelligence and Machine Learning education and research, producing ethical, competent, and socially committed engineers capable of addressing real-world challenges through intelligent systems.",
        styles['AcademicBody']
    ))
    f.append(Spacer(1, 5))

    f.append(Paragraph("<b>Mission of the Department</b>", styles['SectionHeader']))
    f.append(Paragraph(
        "• <b>DM1:</b> Provide comprehensive education and skill development in AI and ML, equipping students with strong engineering knowledge, modern tools, and analytical abilities to solve complex problems.<br/>"
        "• <b>DM2:</b> Foster research, innovation, and design thinking to develop intelligent solutions that address real-world challenges, advance societal welfare, and drive industrial growth.<br/>"
        "• <b>DM3:</b> Promote ethical, professional, and collaborative practices by nurturing teamwork, effective communication, leadership, and adherence to professional ethics.<br/>"
        "• <b>DM4:</b> Encourage lifelong learning, entrepreneurship, and sustainable practices to empower graduates to contribute responsibly to society and global industries.",
        styles['BulletItem']
    ))
    f.append(PageBreak())

    # =========================================================================
    # PAGE 3: TABLE OF CONTENTS
    # =========================================================================
    f.append(Paragraph("<b>TABLE OF CONTENTS</b>", styles['ChapterHeader']))
    f.append(HRFlowable(width="100%", thickness=1.0, color=COLOR_PRIMARY, spaceBefore=2, spaceAfter=6))

    toc_data = [
        [Paragraph("<b>CHAPTER / SECTION TITLE</b>", styles['TableHeader']), Paragraph("<b>PAGE</b>", styles['TableHeader'])],
        [Paragraph("<b>CHAPTER 1: INTRODUCTION</b>", styles['TOCChapter']), Paragraph("<b>6</b>", styles['TOCPageNum'])],
        [Paragraph("1.1 Background &amp; Real-World Motivation", styles['TOCSection']), Paragraph("6", styles['TOCPageNum'])],
        [Paragraph("1.2 Atmospheric Degradation &amp; Optical Physics", styles['TOCSection']), Paragraph("8", styles['TOCPageNum'])],
        [Paragraph("1.3 The Driving Question", styles['TOCSection']), Paragraph("9", styles['TOCPageNum'])],
        [Paragraph("1.4 Project &amp; Pedagogical Objectives", styles['TOCSection']), Paragraph("9", styles['TOCPageNum'])],
        [Paragraph("1.5 Scope, Boundaries, and Limitations", styles['TOCSection']), Paragraph("10", styles['TOCPageNum'])],
        [Paragraph("1.6 Regulatory &amp; Safety Compliance Framework", styles['TOCSection']), Paragraph("10", styles['TOCPageNum'])],
        [Paragraph("<b>CHAPTER 2: LITERATURE SURVEY</b>", styles['TOCChapter']), Paragraph("<b>11</b>", styles['TOCPageNum'])],
        [Paragraph("2.1 Atmospheric Scattering &amp; Dehazing Theory", styles['TOCSection']), Paragraph("11", styles['TOCPageNum'])],
        [Paragraph("2.2 Night Vision, Dynamic Range &amp; Anti-Glare DSP", styles['TOCSection']), Paragraph("13", styles['TOCPageNum'])],
        [Paragraph("2.3 Roadway Geometry, Lane Detection &amp; Potholes", styles['TOCSection']), Paragraph("14", styles['TOCPageNum'])],
        [Paragraph("2.4 Real-Time Object Detection &amp; Kinematic Telemetry", styles['TOCSection']), Paragraph("15", styles['TOCPageNum'])],
        [Paragraph("2.5 Biometric Driver Monitoring Systems (DMS)", styles['TOCSection']), Paragraph("16", styles['TOCPageNum'])],
        [Paragraph("2.6 Comparative Literature Survey Table (35 Systems)", styles['TOCSection']), Paragraph("17", styles['TOCPageNum'])],
        [Paragraph("<b>CHAPTER 3: PROJECT PLANNING AND TEAM ORGANIZATION</b>", styles['TOCChapter']), Paragraph("<b>18</b>", styles['TOCPageNum'])],
        [Paragraph("3.1 12-Week Agile PBL Lifecycle Progress Log", styles['TOCSection']), Paragraph("18", styles['TOCPageNum'])],
        [Paragraph("3.2 System Requirements Specifications (SRS)", styles['TOCSection']), Paragraph("20", styles['TOCPageNum'])],
        [Paragraph("3.3 Multi-Dimensional Feasibility Analysis", styles['TOCSection']), Paragraph("21", styles['TOCPageNum'])],
        [Paragraph("<b>CHAPTER 4: METHODOLOGY</b>", styles['TOCChapter']), Paragraph("<b>23</b>", styles['TOCPageNum'])],
        [Paragraph("4.1 End-to-End System Architecture", styles['TOCSection']), Paragraph("23", styles['TOCPageNum'])],
        [Paragraph("4.2 Iteration 1 - Baseline: Classical DCP", styles['TOCSection']), Paragraph("24", styles['TOCPageNum'])],
        [Paragraph("4.3 Iteration 2 - Refinement: Fast Guided Filter", styles['TOCSection']), Paragraph("26", styles['TOCPageNum'])],
        [Paragraph("4.4 Iteration 3 &amp; Final Approach: The OmniVision Engine", styles['TOCSection']), Paragraph("28", styles['TOCPageNum'])],
        [Paragraph("4.5 Formal Mathematical Derivations", styles['TOCSection']), Paragraph("32", styles['TOCPageNum'])],
        [Paragraph("4.6 YOLOv8 Training, Quantization &amp; Optimization", styles['TOCSection']), Paragraph("32", styles['TOCPageNum'])],
        [Paragraph("<b>CHAPTER 5: IMPLEMENTATION</b>", styles['TOCChapter']), Paragraph("<b>33</b>", styles['TOCPageNum'])],
        [Paragraph("5.1 Comprehensive Modular Decomposition", styles['TOCSection']), Paragraph("33", styles['TOCPageNum'])],
        [Paragraph("5.2 Key Code Listings with Technical Annotations", styles['TOCSection']), Paragraph("35", styles['TOCPageNum'])],
        [Paragraph("5.3 Cyber Cockpit HUD &amp; Dual Navigation UI", styles['TOCSection']), Paragraph("39", styles['TOCPageNum'])],
        [Paragraph("<b>CHAPTER 6: RESULTS AND DISCUSSION</b>", styles['TOCChapter']), Paragraph("<b>40</b>", styles['TOCPageNum'])],
        [Paragraph("6.1 Evaluation Metrics &amp; Experimental Setup", styles['TOCSection']), Paragraph("40", styles['TOCPageNum'])],
        [Paragraph("6.2 Cross-Iteration Quantitative Benchmark Comparison", styles['TOCSection']), Paragraph("41", styles['TOCPageNum'])],
        [Paragraph("6.3 Real-World Adverse Driving Road Tests", styles['TOCSection']), Paragraph("42", styles['TOCPageNum'])],
        [Paragraph("6.4 Cross-Platform Hardware Benchmarks", styles['TOCSection']), Paragraph("46", styles['TOCPageNum'])],
        [Paragraph("6.5 Failure Modes, Edge Cases &amp; Ablation Studies", styles['TOCSection']), Paragraph("47", styles['TOCPageNum'])],
        [Paragraph("<b>CHAPTER 7: TEAM REFLECTION AND LEARNING OUTCOMES</b>", styles['TOCChapter']), Paragraph("<b>48</b>", styles['TOCPageNum'])],
        [Paragraph("7.1 Individual Pedagogical &amp; Technical Reflections", styles['TOCSection']), Paragraph("48", styles['TOCPageNum'])],
        [Paragraph("7.2 Team Learning, Dynamics &amp; Pivot Decision", styles['TOCSection']), Paragraph("49", styles['TOCPageNum'])],
        [Paragraph("7.3 Course Outcomes - Evidence Summary", styles['TOCSection']), Paragraph("50", styles['TOCPageNum'])],
        [Paragraph("<b>CHAPTER 8: CONCLUSION AND FUTURE SCOPE</b>", styles['TOCChapter']), Paragraph("<b>51</b>", styles['TOCPageNum'])],
        [Paragraph("8.1 Concluding Synthesis &amp; Objectives Fulfillment", styles['TOCSection']), Paragraph("51", styles['TOCPageNum'])],
        [Paragraph("8.2 Future Scope &amp; Commercialization Roadmap", styles['TOCSection']), Paragraph("52", styles['TOCPageNum'])],
        [Paragraph("<b>REFERENCES</b>", styles['TOCChapter']), Paragraph("<b>53</b>", styles['TOCPageNum'])],
        [Paragraph("<b>APPENDIX (A.1 to A.5)</b>", styles['TOCChapter']), Paragraph("<b>54</b>", styles['TOCPageNum'])],
    ]
    t_toc = Table(toc_data, colWidths=[USABLE_WIDTH * 0.88, USABLE_WIDTH * 0.12])
    t_toc.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), COLOR_PRIMARY),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('TOPPADDING', (0, 0), (-1, -1), 1.2),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 1.2),
        ('LEFTPADDING', (0, 0), (-1, -1), 2),
        ('RIGHTPADDING', (0, 0), (-1, -1), 2),
        ('LINEBELOW', (0, 0), (-1, -1), 0.3, colors.HexColor('#E2E8F0')),
    ]))
    f.append(t_toc)
    f.append(PageBreak())

    # =========================================================================
    # PAGE 4: LIST OF FIGURES
    # =========================================================================
    f.append(Paragraph("<b>LIST OF FIGURES</b>", styles['ChapterHeader']))
    f.append(HRFlowable(width="100%", thickness=1.0, color=COLOR_PRIMARY, spaceBefore=2, spaceAfter=8))

    lof_data = [
        [Paragraph("<b>FIGURE NUMBER &amp; CAPTION</b>", styles['TableHeader']), Paragraph("<b>PAGE</b>", styles['TableHeader'])],
        [Paragraph("Figure 1.1 Adverse Weather Incident Taxonomy on Indian Highways", styles['IndexEntry']), Paragraph("6", styles['TOCPageNum'])],
        [Paragraph("Figure 1.2 Koschmieder Atmospheric Scattering Optical Rays", styles['IndexEntry']), Paragraph("8", styles['TOCPageNum'])],
        [Paragraph("Figure 2.1 DCP Soft Matting vs. Guided Filter Transmission Map", styles['IndexEntry']), Paragraph("12", styles['TOCPageNum'])],
        [Paragraph("Figure 2.2 Retinex Illumination-Reflectance Decomposition", styles['IndexEntry']), Paragraph("13", styles['TOCPageNum'])],
        [Paragraph("Figure 2.3 Canny Edge &amp; Probabilistic Hough Lane Extraction", styles['IndexEntry']), Paragraph("14", styles['TOCPageNum'])],
        [Paragraph("Figure 2.4 Pinhole Camera Ground-Plane Metric Distance Model", styles['IndexEntry']), Paragraph("15", styles['TOCPageNum'])],
        [Paragraph("Figure 2.5 MediaPipe 468-Point Biometric Facial Landmark Topology", styles['IndexEntry']), Paragraph("16", styles['TOCPageNum'])],
        [Paragraph("Figure 4.1 ClearDrive OmniVision End-to-End System Architecture", styles['IndexEntry']), Paragraph("23", styles['TOCPageNum'])],
        [Paragraph("Figure 4.2 Asynchronous Decoupled Thread Worker Pipeline", styles['IndexEntry']), Paragraph("26", styles['TOCPageNum'])],
        [Paragraph("Figure 4.3 Baseline Iteration 1 Bottleneck Profiling", styles['IndexEntry']), Paragraph("25", styles['TOCPageNum'])],
        [Paragraph("Figure 4.4 Refined Iteration 2 Fast Guided Filter Data Flow", styles['IndexEntry']), Paragraph("26", styles['TOCPageNum'])],
        [Paragraph("Figure 4.5 Gyroscopic Vibration Counter-Shift Trajectory", styles['IndexEntry']), Paragraph("29", styles['TOCPageNum'])],
        [Paragraph("Figure 4.6 Kinematic +1.5s Ghost-Vision Vector Projection", styles['IndexEntry']), Paragraph("31", styles['TOCPageNum'])],
        [Paragraph("Figure 5.1 Cyber Cockpit HUD Dual Navigation Split Layout", styles['IndexEntry']), Paragraph("39", styles['TOCPageNum'])],
        [Paragraph("Figure 6.1 Throughput (FPS) Comparison Across Iterations", styles['IndexEntry']), Paragraph("41", styles['TOCPageNum'])],
        [Paragraph("Figure 6.2 PSNR and SSIM Dehazing Quality Across Weather Modes", styles['IndexEntry']), Paragraph("41", styles['TOCPageNum'])],
        [Paragraph("Figure 6.3 Ground-Truth vs. ClearDrive Metric Distance Calibration", styles['IndexEntry']), Paragraph("46", styles['TOCPageNum'])],
    ]
    t_lof = Table(lof_data, colWidths=[USABLE_WIDTH * 0.88, USABLE_WIDTH * 0.12])
    t_lof.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), COLOR_SECONDARY),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('TOPPADDING', (0, 0), (-1, -1), 2.8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2.8),
        ('LINEBELOW', (0, 0), (-1, -1), 0.3, colors.HexColor('#E2E8F0')),
    ]))
    f.append(t_lof)
    f.append(PageBreak())

    # =========================================================================
    # PAGE 5: LIST OF TABLES & LIST OF ABBREVIATIONS
    # =========================================================================
    f.append(Paragraph("<b>LIST OF TABLES</b>", styles['ChapterHeader']))
    f.append(HRFlowable(width="100%", thickness=0.8, color=COLOR_PRIMARY, spaceBefore=1, spaceAfter=4))

    lot_data = [
        [Paragraph("<b>TABLE NUMBER &amp; TITLE</b>", styles['TableHeader']), Paragraph("<b>PAGE</b>", styles['TableHeader'])],
        [Paragraph("Table 2.1 Exhaustive Comparative Survey of 35 ADAS Solutions", styles['IndexEntry']), Paragraph("17", styles['TOCPageNum'])],
        [Paragraph("Table 3.1 12-Week Agile PBL Lifecycle Progress Log", styles['IndexEntry']), Paragraph("18", styles['TOCPageNum'])],
        [Paragraph("Table 3.2 Hardware and Software Requirements Specification (SRS)", styles['IndexEntry']), Paragraph("20", styles['TOCPageNum'])],
        [Paragraph("Table 3.3 ClearDrive BOM vs. Commercial OEM ADAS Cost", styles['IndexEntry']), Paragraph("22", styles['TOCPageNum'])],
        [Paragraph("Table 6.1 Model Performance Across Engineering Iterations", styles['IndexEntry']), Paragraph("41", styles['TOCPageNum'])],
        [Paragraph("Table 6.2 Cross-Platform Compute &amp; Latency Benchmarks", styles['IndexEntry']), Paragraph("46", styles['TOCPageNum'])],
        [Paragraph("Table 6.3 Ablation Study of Core Perception Filters", styles['IndexEntry']), Paragraph("47", styles['TOCPageNum'])],
        [Paragraph("Table 7.1 Course Outcomes (CO) to PO Evidence Matrix", styles['IndexEntry']), Paragraph("50", styles['TOCPageNum'])],
        [Paragraph("Table A.1 Self and Peer Assessment Quantitative Rubric", styles['IndexEntry']), Paragraph("55", styles['TOCPageNum'])],
    ]
    t_lot = Table(lot_data, colWidths=[USABLE_WIDTH * 0.88, USABLE_WIDTH * 0.12])
    t_lot.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), COLOR_PRIMARY),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('TOPPADDING', (0, 0), (-1, -1), 1.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 1.5),
        ('LINEBELOW', (0, 0), (-1, -1), 0.3, colors.HexColor('#E2E8F0')),
    ]))
    f.append(t_lot)
    f.append(Spacer(1, 6))

    f.append(Paragraph("<b>LIST OF ABBREVIATIONS</b>", styles['ChapterHeader']))
    f.append(HRFlowable(width="100%", thickness=0.8, color=COLOR_SECONDARY, spaceBefore=1, spaceAfter=4))

    # Two column table with abbreviations
    abbr_left = [
        ("ADAS", "Advanced Driver Assistance Systems"),
        ("AIS", "Automotive Industry Standards (India)"),
        ("ASIL", "Automotive Safety Integrity Level (ISO 26262)"),
        ("BOM", "Bill of Materials"),
        ("CLAHE", "Contrast Limited Adaptive Histogram Eq."),
        ("CMOS", "Complementary Metal-Oxide Semiconductor"),
        ("CNN", "Convolutional Neural Network"),
        ("C-V2X", "Cellular Vehicle-to-Everything (3GPP Rel-16)"),
        ("DCP", "Dark Channel Prior"),
        ("DMS", "Driver Monitoring System"),
        ("DSRC", "Dedicated Short-Range Communications"),
        ("EAR", "Eye Aspect Ratio"),
        ("EMA", "Exponential Moving Average"),
        ("FLIR", "Forward-Looking Infrared"),
        ("FOV", "Field of View"),
        ("FPS", "Frames Per Second"),
        ("GF", "Guided Filter / Fast Guided Filter"),
        ("GFLOPs", "Giga Floating-Point Operations Per Sec"),
        ("GPS", "Global Positioning System"),
    ]

    abbr_right = [
        ("HUD", "Heads-Up Display"),
        ("INT8", "8-bit Integer Quantization"),
        ("IPM", "Inverse Perspective Mapping"),
        ("JSON", "JavaScript Object Notation"),
        ("LiDAR", "Light Detection and Ranging"),
        ("LWIR", "Long-Wave Infrared (8-14 um)"),
        ("MAE", "Mean Absolute Error"),
        ("mAP", "Mean Average Precision"),
        ("MJPEG", "Motion Joint Photographic Experts Group"),
        ("MoRTH", "Ministry of Road Transport & Highways"),
        ("NMS", "Non-Maximum Suppression"),
        ("ODD", "Operational Design Domain"),
        ("PBL", "Project-Based Learning"),
        ("PERCLOS", "Percentage of Eyelid Closure Over Pupil"),
        ("PSNR", "Peak Signal-to-Noise Ratio (dB)"),
        ("REST", "Representational State Transfer"),
        ("ROI", "Region of Interest"),
        ("SRS", "System Requirements Specification"),
        ("SSIM", "Structural Similarity Index Measure"),
    ]

    abbr_combined_data = []
    for (k1, v1), (k2, v2) in zip(abbr_left, abbr_right):
        abbr_combined_data.append([
            Paragraph(f"<b>{k1}</b>", styles['AbbrKey']),
            Paragraph(v1, styles['AbbrVal']),
            Paragraph(f"<b>{k2}</b>", styles['AbbrKey']),
            Paragraph(v2, styles['AbbrVal']),
        ])

    t_abbr = Table(abbr_combined_data, colWidths=[USABLE_WIDTH * 0.12, USABLE_WIDTH * 0.38, USABLE_WIDTH * 0.12, USABLE_WIDTH * 0.38])
    t_abbr.setStyle(TableStyle([
        ('TOPPADDING', (0, 0), (-1, -1), 1.0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 1.0),
        ('LEFTPADDING', (0, 0), (-1, -1), 1),
        ('RIGHTPADDING', (0, 0), (-1, -1), 1),
    ]))
    f.append(t_abbr)
    f.append(PageBreak())

    return f
