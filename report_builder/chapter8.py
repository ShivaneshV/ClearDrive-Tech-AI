"""
Chapter 8 Builder for ClearDrive Tech PBL Report
Generates Pages 91 to 94: Conclusion and Future Scope
8.1 Concluding Synthesis & Objectives Fulfillment
8.2 Future Scope & Research Horizons (C-V2X, Solid-State LiDAR, ASIC)
"""

from reportlab.platypus import Paragraph, Spacer, Table, TableStyle, PageBreak, HRFlowable
from reportlab.lib import colors
from report_builder.styles import (
    USABLE_WIDTH, COLOR_PRIMARY, COLOR_SECONDARY, COLOR_DARK, COLOR_MUTED,
    COLOR_BORDER, create_callout_box
)


def get_chapter8_flowables(styles):
    """Returns flowables for Chapter 8 (Pages 91 to 94)."""
    f = []

    # =========================================================================
    # PAGE 91: CHAPTER 8 COVER & 8.1 CONCLUDING SYNTHESIS
    # =========================================================================
    f.append(Paragraph("<b>CHAPTER 8</b>", styles['ChapterHeader']))
    f.append(Paragraph("<b>CONCLUSION AND FUTURE SCOPE</b>", styles['DocTitle']))
    f.append(HRFlowable(width="100%", thickness=1.5, color=COLOR_PRIMARY, spaceBefore=4, spaceAfter=14))

    f.append(Paragraph("<b>8.1 Concluding Synthesis & Objectives Fulfillment</b>", styles['SectionHeader']))
    f.append(Paragraph(
        "This project set out to resolve a fundamental, life-threatening crisis in vehicular transportation: the vulnerability of drivers and existing Advanced "
        "Driver Assistance Systems (ADAS) when navigating adverse atmospheric environments—specifically dense mountain ghat road fog, blinding monsoon downpours, "
        "pitch-black unlit rural highways, and blinding oncoming LED high-beam glare.",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "Through disciplined, mentor-reviewed Project-Based Learning across twelve intensive weeks, our team conceived, designed, built, and empirically verified "
        "<b>ClearDrive Tech</b>: an edge-computing, physics-guided Omni-Vision Cockpit Operating System and ADAS platform. "
        "We are proud to conclude that all six technical engineering objectives and four pedagogical learning outcomes established in Chapter 1 have been fully "
        "and emphatically fulfilled.",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "<b>Affirmative Answer to the Central Driving Question:</b> We have conclusively demonstrated that an edge-computing, physics-guided deterministic perception "
        "pipeline (Koschmieder DCP + Fast Guided Filter) paired with lightweight asynchronous neural kinematics (YOLOv8n) can eliminate atmospheric degradation, "
        "attenuate blinding high-beam glare, and track road obstacles in real time (<b>35.8 FPS</b>) on standard, low-cost commodity CPU processors drawing under 15W, "
        "without requiring cloud connectivity or multi-lakh sensor suites.",
        styles['AcademicBody']
    ))
    f.append(PageBreak())

    # =========================================================================
    # PAGE 92: SUMMARY OF KEY RESULTS & IMPACT
    # =========================================================================
    f.append(Paragraph("<b>8.1.1 Summary of Key Quantitative Achievements</b>", styles['SubsectionHeader']))
    f.append(Paragraph(
        "The key quantitative outcomes achieved by ClearDrive Tech are summarized below:",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "• <b>Real-Time Throughput & Low Latency:</b> Achieved a sustained <b>35.8 FPS</b> on standard quad-core CPUs with an average end-to-end frame processing "
        "latency of <b>21.8 milliseconds</b>, comfortably satisfying the sub-25ms threshold required for high-speed highway collision avoidance.<br/>"
        "• <b>Radiometric Restoration Quality:</b> Achieved <b>28.4 dB PSNR</b> and <b>0.89 SSIM</b> on challenging mountain fog benchmarks, representing an "
        "unprecedented +10.0 dB radiometric enhancement over raw camera inputs.<br/>"
        "• <b>Neural Object Detection Extension:</b> Increased vehicle detection mAP@0.50 from 54.2% in raw fog to <b>91.4%</b>, extending forward vehicle perception "
        "range from 6 meters out to <b>85 meters</b>.<br/>"
        "• <b>Permanent Resolution of the 'Tree Bug':</b> Dual-space 3D perspective corridor isolation and HSV foliage filtering ($H \\in [20, 95], S \\ge 25$) "
        "permanently reduced pothole false alarms from 14.2 alarms/min to <b>0.0 false alarms/min</b>.<br/>"
        "• <b>Metric Distance & TTC Accuracy:</b> Pinhole ground-plane distance estimation achieved sub-meter accuracy (MAE &lt;0.9m) within 40 meters, while +1.5s "
        "Ghost-Vision successfully alerted drivers to aggressive cut-in threats 1.4 seconds before lane line incursions.<br/>"
        "• <b>Democratized Economic Accessibility:</b> The entire ClearDrive retrofit kit was validated with a Bill of Materials of just <b>Rs. 6,800 ($81.70)</b>—less "
        "than 2% of the cost of commercial OEM luxury thermal systems (Rs. 3,50,000+).",
        styles['BulletItem']
    ))
    f.append(PageBreak())

    # =========================================================================
    # PAGE 93: 8.2 FUTURE SCOPE (HORIZONS 1 & 2)
    # =========================================================================
    f.append(Paragraph("<b>8.2 Future Scope and Research Horizons</b>", styles['SectionHeader']))
    f.append(Paragraph(
        "While ClearDrive Tech represents a fully functional, production-ready ADAS prototype, several promising engineering horizons remain to expand its capabilities:",
        styles['AcademicBody']
    ))
    f.append(Spacer(1, 4))

    f.append(Paragraph("<b>Horizon 1: 3GPP Rel-16 C-V2X 5G NR PC5 Sidelink Integration</b>", styles['SubsectionHeader']))
    f.append(Paragraph(
        "Currently, ClearDrive demonstrates simulated Vehicle-to-Vehicle (V2V) holographic billboards over local Wi-Fi. In future iterations, we plan to interface "
        "ClearDrive directly with automotive 5G NR C-V2X sidelink modems (such as Qualcomm 9150 C-V2X chipset). Operating in the dedicated 5.9 GHz Intelligent "
        "Transportation Systems (ITS) band, vehicles will broadcast high-frequency Basic Safety Messages (BSM) to peer vehicles up to 1 kilometer away. "
        "This will enable cooperative, beyond-line-of-sight collision warnings around blind mountain hairpin bends long before physical optical contact occurs.",
        styles['AcademicBody']
    ))
    f.append(Spacer(1, 4))

    f.append(Paragraph("<b>Horizon 2: Multi-Modal Sensor Fusion with Solid-State MEMS LiDAR</b>", styles['SubsectionHeader']))
    f.append(Paragraph(
        "Emerging solid-state MEMS LiDARs (such as the Livox Mid-360) are dropping in cost toward sub-$200 price points. While optical cameras provide rich semantic "
        "understanding, a sparse LiDAR point cloud provides absolute metric depth. We plan to formulate an Extended Kalman Filter (EKF) sensor fusion pipeline "
        "where sparse LiDAR depth points guide the optical transmission map $t(x)$, eliminating planar road assumptions and delivering sub-centimeter distance "
        "estimation on steep vertical crests.",
        styles['AcademicBody']
    ))
    f.append(PageBreak())

    # =========================================================================
    # PAGE 94: HORIZON 3 & COMMERCIALIZATION ROADMAP
    # =========================================================================
    f.append(Paragraph("<b>Horizon 3: Hardware IP Core Synthesis on FPGA / ASIC</b>", styles['SubsectionHeader']))
    f.append(Paragraph(
        "To achieve automotive ASIL-D functional safety compliance and reduce unit manufacturing costs to under Rs. 1,500 ($18) for mass-market vehicle integration, "
        "we plan to synthesize the Koschmieder Fast Guided Filter, CLAHE, and Canny/Hough DSP pipeline into register-transfer level (RTL) Verilog/VHDL code "
        "for deployment on automotive FPGAs (Xilinx Zynq UltraScale+) or custom silicon ASICs. Hardware acceleration will slash total perception latency to "
        "<b>under 3 milliseconds</b> while consuming less than 2 Watts of power.",
        styles['AcademicBody']
    ))
    f.append(Spacer(1, 6))

    f.append(Paragraph("<b>8.2.1 Commercial Fleet Pilot Deployment Pathway</b>", styles['SubsectionHeader']))
    f.append(Paragraph(
        "Our immediate deployment roadmap includes partnering with regional state transport corporations (such as the State Express Transport Corporation - SETC "
        "and Tamil Nadu State Transport Corporation - TNSTC) to install ClearDrive prototype edge nodes on commercial buses operating regular night and monsoon routes "
        "across the Nilgiris and Western Ghat mountain passes. This real-world fleet trial will collect continuous operational telemetry to validate long-term "
        "component durability and driver behavioral impact.",
        styles['AcademicBody']
    ))
    f.append(Spacer(1, 10))
    f.append(create_callout_box(
        "Final Concluding Thought",
        "True engineering innovation is measured not by how expensive a technology is, but by how effectively it protects human lives. "
        "ClearDrive Tech proves that with mathematical rigor, physics-guided signal processing, and elegant systems architecture, life-saving vehicular safety "
        "can be universal, accessible, and democratized for all.",
        styles
    ))
    f.append(PageBreak())

    return f
