"""
ClearDrive AI: 50-Page Project-Based Learning (PBL) Report Builder
Department of Artificial Intelligence and Machine Learning
Chennai Institute of Technology (Autonomous) | Affiliated to Anna University, Chennai

Strict Rules Enforced:
- EXACTLY 50 Pages (Numbered Page 1 of 50 to Page 50 of 50)
- Zero Index Pages (NO Table of Contents, NO List of Figures, NO List of Tables, NO List of Abbreviations)
- Bonafide Content Alone: Title & Official Bonafide Certificate on Page 1, followed immediately by
  Chapters 1 to 8, References, and Appendices across Pages 2 to 50.
- Shortened Title: CLEARDRIVE AI: REAL-TIME ADAS AND VISION RESTORATION FOR ADVERSE DRIVING CONDITIONS
- Currency formatting fixed as 'Rs.' (Zero black box characters)
"""

import sys
import os
import pypdf

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, HRFlowable

# Page Dimensions
PAGE_WIDTH, PAGE_HEIGHT = A4
MARGIN_LEFT = 54.0    # 0.75 in (binding margin)
MARGIN_RIGHT = 45.0   # ~0.62 in
MARGIN_TOP = 50.0
MARGIN_BOTTOM = 50.0
USABLE_WIDTH = PAGE_WIDTH - MARGIN_LEFT - MARGIN_RIGHT
USABLE_HEIGHT = PAGE_HEIGHT - MARGIN_TOP - MARGIN_BOTTOM

# Academic Color Palette
COLOR_PRIMARY = colors.HexColor('#0F2A4A')    # Deep Academic Navy
COLOR_SECONDARY = colors.HexColor('#1E56A0')  # Academic Royal Blue
COLOR_DARK = colors.HexColor('#1A1A1A')       # Charcoal Body Text
COLOR_MUTED = colors.HexColor('#4B5563')      # Secondary Grey
COLOR_BORDER = colors.HexColor('#CBD5E1')     # Clean Slate Border
COLOR_LIGHT_BG = colors.HexColor('#F8FAFC')   # Subtle Table/Code Background


class NumberedCanvas50(canvas.Canvas):
    """
    Two-pass canvas that renders running headers and footers with
    dynamic 'Page X of 50' pagination across all 50 pages.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, page_count):
        # Suppress running headers on Page 1 (Cover / Bonafide Certificate)
        if self._pageNumber == 1:
            return

        self.saveState()
        
        # --- RUNNING HEADER ---
        self.setFont("Helvetica-Bold", 7.5)
        self.setFillColor(COLOR_PRIMARY)
        self.drawString(
            MARGIN_LEFT,
            PAGE_HEIGHT - 34,
            "CHENNAI INSTITUTE OF TECHNOLOGY  |  DEPT. OF ARTIFICIAL INTELLIGENCE & MACHINE LEARNING"
        )
        self.setFont("Helvetica", 7.5)
        self.setFillColor(COLOR_MUTED)
        self.drawRightString(
            PAGE_WIDTH - MARGIN_RIGHT,
            PAGE_HEIGHT - 34,
            "CLEARDRIVE AI : PBL REPORT"
        )
        
        # Dividing rule
        self.setStrokeColor(COLOR_BORDER)
        self.setLineWidth(0.5)
        self.line(MARGIN_LEFT, PAGE_HEIGHT - 39, PAGE_WIDTH - MARGIN_RIGHT, PAGE_HEIGHT - 39)

        # --- RUNNING FOOTER ---
        self.line(MARGIN_LEFT, 44, PAGE_WIDTH - MARGIN_RIGHT, 44)
        self.setFont("Helvetica", 7.5)
        self.setFillColor(COLOR_MUTED)
        self.drawString(
            MARGIN_LEFT,
            32,
            "B.E. (AI & ML) — Project-Based Learning (PBL) Component of Machine Learning"
        )
        self.setFont("Helvetica-Bold", 8)
        self.setFillColor(COLOR_PRIMARY)
        self.drawRightString(
            PAGE_WIDTH - MARGIN_RIGHT,
            32,
            f"Page {self._pageNumber} of {page_count}"
        )
        self.restoreState()


def get_styles_50():
    base = getSampleStyleSheet()
    s = {
        'DocTitle': ParagraphStyle('DocTitle', fontName='Helvetica-Bold', fontSize=15, leading=19, textColor=COLOR_PRIMARY, alignment=1, spaceAfter=8),
        'DocSubTitle': ParagraphStyle('DocSubTitle', fontName='Helvetica-Bold', fontSize=10, leading=14, textColor=COLOR_SECONDARY, alignment=1, spaceAfter=8),
        'ChapterHeader': ParagraphStyle('ChapterHeader', fontName='Helvetica-Bold', fontSize=14, leading=18, textColor=COLOR_PRIMARY, spaceBefore=4, spaceAfter=4, keepWithNext=True),
        'SectionHeader': ParagraphStyle('SectionHeader', fontName='Helvetica-Bold', fontSize=11, leading=14, textColor=COLOR_SECONDARY, spaceBefore=6, spaceAfter=3, keepWithNext=True),
        'SubsectionHeader': ParagraphStyle('SubsectionHeader', fontName='Helvetica-Bold', fontSize=9.5, leading=12.5, textColor=COLOR_PRIMARY, spaceBefore=4, spaceAfter=2, keepWithNext=True),
        'AcademicBody': ParagraphStyle('AcademicBody', fontName='Times-Roman', fontSize=9.2, leading=12.5, textColor=COLOR_DARK, alignment=4, spaceAfter=4, firstLineIndent=12),
        'AcademicBodyNoIndent': ParagraphStyle('AcademicBodyNoIndent', fontName='Times-Roman', fontSize=9.2, leading=12.5, textColor=COLOR_DARK, alignment=4, spaceAfter=4),
        'BulletItem': ParagraphStyle('BulletItem', fontName='Times-Roman', fontSize=8.8, leading=11.8, textColor=COLOR_DARK, alignment=4, leftIndent=14, firstLineIndent=-8, spaceAfter=3),
        'MathEquation': ParagraphStyle('MathEquation', fontName='Times-Italic', fontSize=9.2, leading=13, textColor=COLOR_PRIMARY, alignment=1, spaceBefore=4, spaceAfter=4),
        'CodeSnippet': ParagraphStyle('CodeSnippet', fontName='Courier', fontSize=7.2, leading=9.2, textColor=colors.HexColor('#1E293B'), spaceBefore=2, spaceAfter=2),
        'TableHeader': ParagraphStyle('TableHeader', fontName='Helvetica-Bold', fontSize=8.0, leading=10, textColor=colors.white, alignment=1),
        'TableCell': ParagraphStyle('TableCell', fontName='Times-Roman', fontSize=7.5, leading=9.5, textColor=COLOR_DARK, alignment=0),
        'TableCellCenter': ParagraphStyle('TableCellCenter', fontName='Times-Roman', fontSize=7.5, leading=9.5, textColor=COLOR_DARK, alignment=1),
        'TableCellBold': ParagraphStyle('TableCellBold', fontName='Helvetica-Bold', fontSize=7.5, leading=9.5, textColor=COLOR_PRIMARY, alignment=0),
        'TableCaption': ParagraphStyle('TableCaption', fontName='Helvetica-Bold', fontSize=8.0, leading=10.5, textColor=COLOR_PRIMARY, alignment=1, spaceBefore=4, spaceAfter=2, keepWithNext=True),
        'FigureCaption': ParagraphStyle('FigureCaption', fontName='Helvetica-Bold', fontSize=8.0, leading=10.5, textColor=COLOR_PRIMARY, alignment=1, spaceBefore=2, spaceAfter=4),
        'CalloutText': ParagraphStyle('CalloutText', fontName='Times-Italic', fontSize=8.6, leading=11.6, textColor=COLOR_DARK, spaceBefore=2, spaceAfter=2),
        'ReferenceEntry': ParagraphStyle('ReferenceEntry', fontName='Times-Roman', fontSize=7.5, leading=9.8, textColor=COLOR_DARK, leftIndent=16, firstLineIndent=-16, spaceAfter=2.5)
    }
    return s


def create_code_block(code_text, styles, width=USABLE_WIDTH):
    p = Paragraph(code_text.replace('\n', '<br/>').replace(' ', '&nbsp;'), styles['CodeSnippet'])
    t = Table([[p]], colWidths=[width])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#F1F5F9')),
        ('BOX', (0, 0), (-1, -1), 0.6, colors.HexColor('#CBD5E1')),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
    ]))
    return t


def create_callout_box(title, text, styles, width=USABLE_WIDTH):
    title_p = Paragraph(f"<b>{title}</b>", styles['SubsectionHeader'])
    body_p = Paragraph(text, styles['CalloutText'])
    t = Table([[title_p], [body_p]], colWidths=[width])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#F0F9FF')),
        ('BOX', (0, 0), (-1, -1), 0.8, colors.HexColor('#0284C7')),
        ('LINEBELOW', (0, 0), (-1, 0), 0.4, colors.HexColor('#BAE6FD')),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
    ]))
    return t
