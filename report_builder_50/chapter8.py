"""
Chapter 8: Conclusion and Future Scope (Pages 47 to 48 - Exactly 2 Pages)
ClearDrive AI: Real-Time ADAS and Vision Restoration for Adverse Driving Conditions
"""

from reportlab.platypus import Paragraph, Spacer, Table, TableStyle, PageBreak, HRFlowable
from reportlab.lib import colors
from report_builder_50.styles import (
    USABLE_WIDTH, COLOR_PRIMARY, COLOR_SECONDARY, COLOR_BORDER,
    create_callout_box
)


def get_chapter8_flowables(styles):
    """Returns flowables for Chapter 8 (Pages 47 to 48 - Exactly 2 Pages)."""
    f = []

    # =========================================================================
    # PAGE 47: CHAPTER 8 COVER & 8.1 FULFILLMENT OF OBJECTIVES
    # =========================================================================
    f.append(Paragraph("<b>CHAPTER 8</b>", styles['ChapterHeader']))
    f.append(Paragraph("<b>CONCLUSION AND FUTURE SCOPE</b>", styles['DocTitle']))
    f.append(HRFlowable(width="100%", thickness=1.2, color=COLOR_PRIMARY, spaceBefore=2, spaceAfter=8))

    f.append(Paragraph("<b>8.1 Fulfillment of Project and Pedagogical Objectives</b>", styles['SectionHeader']))
    f.append(Paragraph(
        "ClearDrive AI successfully resolves the foundational driving question established at the inception of this Project-Based Learning endeavor. "
        "By fusing classical atmospheric radiative transfer physics with modern edge deep learning and lock-free multiprocessing concurrency, "
        "the project demonstrates that publication-grade adverse weather perception can be achieved on low-cost consumer hardware without requiring "
        "prohibitively expensive LiDAR or thermal sensor suites.",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "<b>Synthesis of Objective Attainments:</b><br/>"
        "• <b>RO1 (Real-Time Physics Restoration):</b> Successfully engineered an $O(N)$ linear-time restoration engine based on the Dark Channel Prior (DCP) "
        "and Fast Guided Filter. The formulation achieved a $16,000\\times$ acceleration over classical Soft Matting, reaching <b>38.6 FPS</b> on x86 and "
        "<b>32.4 FPS</b> on a Raspberry Pi 4B. The introduction of the Adaptive Luminance Floor and temporal EMA airlight smoothing permanently eliminated "
        "the 'Tree Bug' canopy halos and atmospheric flickering.<br/>"
        "• <b>RO2 (Zero-Light &amp; Anti-Glare DSP):</b> Developed Starlight HDR 'Ghost-Vision' using YUV-decoupled CLAHE with black pedestal protection, "
        "expanding nighttime optical awareness by 300% (detecting unlit pedestrians at 42 meters in 0.08 lux). Polarized Anti-Glare knee compression compressed "
        "high-beam blooming halos by 68.4%, preserving critical drivable roadway geometry.<br/>"
        "• <b>RO3 (Neural Kinematics &amp; Telemetry):</b> Quantized YOLOv8n coupled with monocular pinhole ground geometry delivered real-time distance $Z$ "
        "with &lt;8% error up to 40 meters, while dynamic Time-to-Collision (TTC) alerted drivers 3.6 seconds ahead of impending collisions.<br/>"
        "• <b>RO4 (Structural Safety &amp; Biometric DMS):</b> Projected augmented reality (AR) neon-cyan lane carpets, color-coded pothole depth hazard boxes, "
        "and monitored driver alertness via 468-point 3D facial mesh eyelid EAR, detecting microsleep episodes within 0.67 seconds.<br/>"
        "• <b>RO5 (Economic Accessibility):</b> Packaged the complete system into an edge Bill of Materials of <b>Rs. 6,800</b>-representing a &gt;97% cost reduction "
        "compared to enterprise OEM ADAS solutions-and fully open-sourced the codebase on GitHub under the permissive MIT license.",
        styles['AcademicBody']
    ))
    f.append(PageBreak())

    # =========================================================================
    # PAGE 48: 8.2 FUTURE RESEARCH DIRECTIONS & FINAL REMARKS
    # =========================================================================
    f.append(Paragraph("<b>8.2 Future Research Directions and Next-Generation Upgrades</b>", styles['SectionHeader']))
    f.append(Paragraph(
        "While ClearDrive AI has achieved all operational objectives, several high-impact research frontiers warrant exploration:",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "<b>1. Cellular Vehicle-to-Everything (C-V2X) 5G NR Sidelink:</b> Future iterations will integrate direct PC5 sidelink communication. "
        "When an edge vehicle detects a road hazard (e.g., severe dense fog bank, major pothole, or stalled vehicle), it will broadcast a localized "
        "Cooperative Awareness Message (CAM) to oncoming vehicles via 5G NR sidelink, alerting drivers before obstacles enter their physical line of sight.",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "<b>2. Solid-State MEMS LiDAR Low-Level Feature Fusion:</b> Emerging solid-state micro-LiDAR sensors (costing &lt;Rs. 15,000) can provide sparse depth cues. "
        "Fusing sparse micro-LiDAR depth points directly into the Fast Guided Filter's transmission map estimation will provide absolute ground-truth depth anchors, "
        "further refining restoration under zero-texture conditions.",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "<b>3. Dedicated Automotive ASIC / FPGA Acceleration:</b> Synthesizing the Fast Guided Filter and YOLOv8 pipeline onto embedded AI co-processors "
        "(such as Hailo-8 or Xilinx Kria SOM) will slash power consumption below 5 Watts while boosting throughput to <b>&gt;120 FPS at 1080p resolution</b>, "
        "enabling direct tier-1 automotive integration.",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "<b>4. Fleet-Wide Federated Learning:</b> Implementing decentralized federated learning across commercial fleet edge nodes will allow continuous "
        "fine-tuning of edge neural weights on rare Indian road anomalies (e.g., specialized agricultural machinery, unpaved diversions) with zero raw video upload, "
        "preserving total driver privacy.",
        styles['AcademicBody']
    ))
    f.append(Spacer(1, 4))
    f.append(create_callout_box(
        "Final Concluding Remark",
        "ClearDrive AI stands as proof that software-defined edge intelligence can democratize automotive safety. "
        "By restoring sight where human eyes and conventional sensors fail, this project offers an accessible, life-saving shield "
        "for the millions of drivers who navigate adverse road conditions every day.",
        styles
    ))
    f.append(PageBreak())

    return f
