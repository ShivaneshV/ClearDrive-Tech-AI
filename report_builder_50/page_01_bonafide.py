"""
Page 1: Formal Title & Official Bonafide Certificate
Chennai Institute of Technology (Autonomous) | Department of AI & ML
Strict Rules: Title, Submission, and Official Bonafide Sign-Off fit on Page 1.
"""

from reportlab.platypus import Paragraph, Spacer, Table, TableStyle, PageBreak, HRFlowable
from reportlab.lib import colors
from report_builder_50.styles import (
    USABLE_WIDTH, COLOR_PRIMARY, COLOR_SECONDARY, COLOR_BORDER
)


def get_page_01_flowables(styles):
    """Returns flowables for Page 1 (Title Page & Official Bonafide Certificate)."""
    f = []

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
    f.append(Paragraph("<b>SHIVANESH V</b> [Reg. No. 210423243050] &nbsp;&nbsp;&nbsp;&nbsp; <b>CO-RESEARCHER</b> [Reg. No. 210423243051]", styles['SubsectionHeader']))
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
        "is a bonafide record of work carried out by <b>SHIVANESH V (Reg. No: 210423243050)</b> and <b>CO-RESEARCHER (Reg. No: 210423243051)</b> of the Department of "
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
    return f
