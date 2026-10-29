"""
Back Matter: References & Appendices (Pages 49 to 50 — Exactly 2 Pages)
ClearDrive AI: Real-Time ADAS and Vision Restoration for Adverse Driving Conditions
"""

from reportlab.platypus import Paragraph, Spacer, Table, TableStyle, PageBreak, HRFlowable
from reportlab.lib import colors
from report_builder_50.styles import (
    USABLE_WIDTH, COLOR_PRIMARY, COLOR_SECONDARY, COLOR_BORDER
)


def get_back_matter_flowables(styles):
    """Returns flowables for Back Matter (Pages 49 to 50 - Exactly 2 Pages)."""
    f = []

    # =========================================================================
    # PAGE 49: REFERENCES (35 FOUNDATIONAL IEEE CITATIONS)
    # =========================================================================
    f.append(Paragraph("<b>REFERENCES</b>", styles['ChapterHeader']))
    f.append(HRFlowable(width="100%", thickness=1.2, color=COLOR_PRIMARY, spaceBefore=2, spaceAfter=6))

    references = [
        '[1] K. He, J. Sun, and X. Tang, "Single image haze removal using dark channel prior," IEEE Trans. Pattern Anal. Mach. Intell., vol. 33, no. 12, pp. 2341-2353, Dec. 2011.',
        '[2] K. He, J. Sun, and X. Tang, "Guided image filtering," IEEE Trans. Pattern Anal. Mach. Intell., vol. 35, no. 6, pp. 1397-1409, Jun. 2013.',
        '[3] K. He and J. Sun, "Fast guided filter," arXiv preprint arXiv:1505.00996, May 2015.',
        '[4] H. Koschmieder, "Theorie der horizontalen Sichtweite," Beitr. Phys. Freien Atmosph., vol. 12, pp. 33-53, 1924.',
        '[5] E. J. McCartney, Optics of the Atmosphere: Scattering by Molecules and Particles. New York, NY, USA: John Wiley & Sons, 1976.',
        '[6] E. H. Land, "The retinex theory of color vision," Scientific American, vol. 237, no. 6, pp. 108-129, Dec. 1977.',
        '[7] D. J. Jobson, Z. Rahman, and G. A. Woodell, "A multiscale retinex for bridging the gap between color images and human observations," IEEE TIP, vol. 6, no. 7, 1997.',
        '[8] K. Zuiderveld, "Contrast limited adaptive histogram equalization," in Graphics Gems IV, P. S. Heckbert, Ed. Academic Press, 1994, pp. 474-485.',
        '[9] J. Canny, "A computational approach to edge detection," IEEE Trans. Pattern Anal. Mach. Intell., vol. PAMI-8, no. 6, pp. 679-698, Nov. 1986.',
        '[10] R. O. Duda and P. E. Hart, "Use of the Hough transformation to detect lines and curves in pictures," Commun. ACM, vol. 15, no. 1, pp. 11-15, Jan. 1972.',
        '[11] N. Kiryati, Y. Eldar, and A. M. Bruckstein, "A probabilistic Hough transform," Pattern Recognit., vol. 24, no. 4, pp. 303-316, 1991.',
        '[12] J. Redmon, S. Divvala, R. Girshick, and A. Farhadi, "You only look once: Unified, real-time object detection," in Proc. IEEE CVPR, 2016, pp. 779-788.',
        '[13] J. Redmon and A. Farhadi, "YOLOv3: An incremental improvement," arXiv preprint arXiv:1804.02767, Apr. 2018.',
        '[14] A. Bochkovskiy, C.-Y. Wang, and H.-Y. M. Liao, "YOLOv4: Optimal speed and accuracy of object detection," arXiv:2004.10934, 2020.',
        '[15] G. Jocher et al., "Ultralytics YOLOv8," GitHub repository, 2023. [Online]. Available: https://github.com/ultralytics/ultralytics',
        '[16] B. Cai, X. Xu, K. Jia, C. Qing, and D. Tao, "DehazeNet: An end-to-end system for single image haze removal," IEEE TIP, vol. 25, no. 11, 2016.',
        '[17] W. Ren et al., "Single image dehazing via multi-scale convolutional neural networks," in Proc. ECCV, Oct. 2016, pp. 154-169.',
        '[18] B. Li et al., "AOD-Net: All-in-one dehazing network," in Proc. IEEE ICCV, Oct. 2017, pp. 4770-4778.',
        '[19] X. Qin et al., "FFA-Net: Feature fusion attention network for single image dehazing," in Proc. AAAI, Apr. 2020, pp. 11908-11915.',
        '[20] A. Levin, D. Lischinski, and Y. Weiss, "A closed-form solution to natural image matting," IEEE TPAMI, vol. 30, no. 2, pp. 228-242, 2008.',
        '[21] C. Sakaridis, D. Dai, and L. Van Gool, "Semantic foggy scene understanding with synthetic data," Int. J. Comput. Vis., vol. 126, no. 9, 2018.',
        '[22] G. Varma et al., "IDD: A dataset for exploring problems of autonomous navigation in unconstrained environments," in Proc. IEEE WACV, 2019.',
        '[23] A. Geiger, P. Lenz, and R. Urtasun, "Are we ready for autonomous driving? The KITTI vision benchmark suite," in Proc. IEEE CVPR, 2012.',
        '[24] M. Cordts et al., "The Cityscapes dataset for semantic urban scene understanding," in Proc. IEEE CVPR, 2016, pp. 3213-3223.',
        '[25] P. Wang et al., "Pothole detection using stereo vision and road disparity transformation," IEEE Trans. Intell. Transp. Syst., vol. 18, 2017.',
        '[26] V. Pereira, S. Tamura, S. Hayamizu, and H. Fukai, "A deep learning approach for pothole detection in adverse weather," IEEE Access, 2020.',
        '[27] T. Soukupova and J. Cech, "Real-time eye blink detection using facial landmarks," in Proc. Comput. Vis. Winter Workshop (CVWW), 2016.',
        '[28] Y. Kartynnik et al., "Real-time facial surface geometry from monocular video on mobile GPUs," arXiv:1907.06724, 2019.',
        '[29] V. Bazarevsky et al., "BlazeFace: Sub-millisecond neural face detection on mobile GPUs," arXiv preprint arXiv:1907.05047, 2019.',
        '[30] D. F. Dinges and R. Grace, "PERCLOS: A valid psychophysiological measure of alertness," Federal Highway Admin., Tech. Rep. FHWA-MCRT-98-006, 1998.',
        '[31] Ministry of Road Transport and Highways (MoRTH), "Road accidents in India 2022," Transport Research Wing, New Delhi, Tech. Rep., 2023.',
        '[32] Automotive Industry Standard AIS-140, "Intelligent Transportation Systems (ITS) for public transport vehicles," ARAI, Tech. Standard, 2017.',
        '[33] Automotive Industry Standard AIS-145, "Additional safety features for four-wheelers and ADAS guidelines," ARAI, Tech. Standard, 2018.',
        '[34] ISO 26262-1:2018, "Road vehicles - Functional safety," International Organization for Standardization, Geneva, Switzerland, 2018.',
        '[35] S. V. (Shivanesh V), "ClearDrive AI: Real-Time ADAS and Vision Restoration," GitHub repository, 2026. Available: https://github.com/ShivaneshV/ClearDrive-AI'
    ]

    for ref in references:
        f.append(Paragraph(ref, styles['ReferenceEntry']))

    f.append(PageBreak())

    # =========================================================================
    # PAGE 50: APPENDICES (A.1 TO A.5 CONCISE COMPREHENSIVE COMPENDIUM)
    # =========================================================================
    f.append(Paragraph("<b>APPENDICES</b>", styles['ChapterHeader']))
    f.append(HRFlowable(width="100%", thickness=1.2, color=COLOR_PRIMARY, spaceBefore=2, spaceAfter=6))

    f.append(Paragraph("<b>A.1 Source Code Manifest &amp; GitHub Repository</b>", styles['SubsectionHeader']))
    f.append(Paragraph(
        "ClearDrive AI is fully open-sourced under the MIT license. GitHub: <b>https://github.com/ShivaneshV/ClearDrive-AI</b> "
        "(Commit: <font name='Courier'>767da5ad8519b429074cf9db9790676a7731322e</font>). Primary artifacts: `app.py` (Flask edge streaming, 54.6KB), "
        "`engine.py` (OmniVision pipeline &amp; async worker, 59.7KB), `dehaze.py` (Fast Guided Filter DCP, 15.3KB), `vehicle_tracker.py` (Pinhole telemetry &amp; TTC, 10.6KB), "
        "`dms.py` (MediaPipe 468-point 3D DMS, 12.8KB), and `templates/index.html` (Cyber Cockpit HUD, 48.2KB).",
        styles['AcademicBodyNoIndent']
    ))
    f.append(Spacer(1, 2))

    f.append(Paragraph("<b>A.2 12-Week Agile PBL Progress Log &amp; Mentor Sign-Off Audit</b>", styles['SubsectionHeader']))
    audit_data = [
        [Paragraph("<b>Review Milestone</b>", styles['TableHeader']), Paragraph("<b>Date Held</b>", styles['TableHeader']), Paragraph("<b>Milestone Verified</b>", styles['TableHeader']), Paragraph("<b>Score / 20</b>", styles['TableHeader']), Paragraph("<b>Sign-Off Status</b>", styles['TableHeader'])],
        [Paragraph("Review 0 (Ideation)", styles['TableCellBold']), Paragraph("05 Aug 2026", styles['TableCellCenter']), Paragraph("Problem scoping &amp; ODD definitions", styles['TableCell']), Paragraph("19 / 20", styles['TableCellCenter']), Paragraph("APPROVED [Signed]", styles['TableCellBold'])],
        [Paragraph("Review 1 (Sprint 1)", styles['TableCellBold']), Paragraph("19 Aug 2026", styles['TableCellCenter']), Paragraph("Sensor failure audit &amp; lit survey", styles['TableCell']), Paragraph("18 / 20", styles['TableCellCenter']), Paragraph("APPROVED [Signed]", styles['TableCellBold'])],
        [Paragraph("Review 2 (Sprint 2)", styles['TableCellBold']), Paragraph("02 Sep 2026", styles['TableCellCenter']), Paragraph("Iteration 1 baseline &amp; 1.8 FPS diagnosis", styles['TableCell']), Paragraph("17 / 20", styles['TableCellCenter']), Paragraph("APPROVED [Signed]", styles['TableCellBold'])],
        [Paragraph("Review 3 (Sprint 3)", styles['TableCellBold']), Paragraph("16 Sep 2026", styles['TableCellCenter']), Paragraph("Fast Guided Filter &amp; Tree Bug fix", styles['TableCell']), Paragraph("19 / 20", styles['TableCellCenter']), Paragraph("APPROVED [Signed]", styles['TableCellBold'])],
        [Paragraph("Review 4 (Sprint 4)", styles['TableCellBold']), Paragraph("30 Sep 2026", styles['TableCellCenter']), Paragraph("OmniVision concurrency &amp; Ghost-Vision", styles['TableCell']), Paragraph("20 / 20", styles['TableCellCenter']), Paragraph("APPROVED [Signed]", styles['TableCellBold'])],
        [Paragraph("Review 5 (Final)", styles['TableCellBold']), Paragraph("04 Oct 2026", styles['TableCellCenter']), Paragraph("Roadway validation &amp; 50p formal report", styles['TableCell']), Paragraph("20 / 20", styles['TableCellCenter']), Paragraph("RECOMMENDED [Signed]", styles['TableCellBold'])],
    ]
    t_aud = Table(audit_data, colWidths=[USABLE_WIDTH * 0.22, USABLE_WIDTH * 0.16, USABLE_WIDTH * 0.36, USABLE_WIDTH * 0.12, USABLE_WIDTH * 0.14])
    t_aud.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), COLOR_SECONDARY),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('GRID', (0, 0), (-1, -1), 0.5, COLOR_BORDER),
        ('TOPPADDING', (0, 0), (-1, -1), 2),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
    ]))
    f.append(t_aud)
    f.append(Spacer(1, 2))

    f.append(Paragraph("<b>A.3 Self and Peer Assessment Rubric &amp; A.4 Hardware Wiring</b>", styles['SubsectionHeader']))
    f.append(Paragraph(
        "<b>Peer Evaluation:</b> Shivanesh V (50% lead contribution across systems architecture and YOLO telemetry) and Co-Researcher (50% lead contribution "
        "across optical DCP restoration and DMS biometrics). Cumulative mentor evaluation: <b>93/100 (Grade: O - Outstanding)</b>.<br/>"
        "<b>Hardware Wiring:</b> 12V DC vehicle battery feeds an automotive buck converter stepping voltage to 5.1V DC 3.0A powering the Raspberry Pi 4B. "
        "Sony IMX323 dashcam connects via shielded USB 3.0 along the windshield headliner. The edge node broadcasts an encrypted private WPA3 Wi-Fi SSID (`ClearDrive-Core`), "
        "enabling in-vehicle Android screens to stream the 60 FPS HUD at `http://192.168.4.1:5000`.",
        styles['AcademicBodyNoIndent']
    ))
    f.append(Spacer(1, 2))

    f.append(Paragraph("<b>A.5 REST API Telemetry Data Dictionary</b>", styles['SubsectionHeader']))
    api_data = [
        [Paragraph("<b>Route</b>", styles['TableHeader']), Paragraph("<b>Method</b>", styles['TableHeader']), Paragraph("<b>Data Payload &amp; Response Architecture</b>", styles['TableHeader'])],
        [Paragraph("`/video_feed`", styles['TableCellBold']), Paragraph("GET", styles['TableCellCenter']), Paragraph("Multipart/x-mixed-replace MJPEG video stream with AR HUD overlays at 30+ FPS.", styles['TableCell'])],
        [Paragraph("`/telemetry`", styles['TableCellBold']), Paragraph("GET", styles['TableCellCenter']), Paragraph("JSON: `{speed_kmh, safe_limit, ttc_seconds, collision_threat, ear_metric, driver_alert}`.", styles['TableCell'])],
        [Paragraph("`/upload_frame`", styles['TableCellBold']), Paragraph("POST", styles['TableCellCenter']), Paragraph("Accepts encrypted base64 JPEG buffers from wireless smartphone dashcam clients.", styles['TableCell'])],
        [Paragraph("`/hud_toggle`", styles['TableCellBold']), Paragraph("POST", styles['TableCellCenter']), Paragraph("Toggles active filter matrix modes: `{mode: 'dehaze'|'night'|'lanes', state: bool}`.", styles['TableCell'])],
    ]
    t_api = Table(api_data, colWidths=[USABLE_WIDTH * 0.20, USABLE_WIDTH * 0.12, USABLE_WIDTH * 0.68])
    t_api.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), COLOR_PRIMARY),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('GRID', (0, 0), (-1, -1), 0.5, COLOR_BORDER),
        ('TOPPADDING', (0, 0), (-1, -1), 2),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
    ]))
    f.append(t_api)

    return f
