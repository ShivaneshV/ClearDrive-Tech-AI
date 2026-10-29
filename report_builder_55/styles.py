"""
ClearDrive AI: 55-Page Academic Styles and Typography
Chennai Institute of Technology (Autonomous) | Department of AI & ML
Strictly 55 Pages with complete preliminary matter, TOC, LOF, LOT, and Abbreviations.
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph, Table, TableStyle

# Page Dimensions (A4: 595.28 x 841.89 pt)
PAGE_WIDTH, PAGE_HEIGHT = A4
MARGIN_LEFT = 54.0    # 0.75 in (binding margin)
MARGIN_RIGHT = 45.0   # ~0.62 in
MARGIN_TOP = 50.0
MARGIN_BOTTOM = 50.0
USABLE_WIDTH = PAGE_WIDTH - MARGIN_LEFT - MARGIN_RIGHT    # 496.28 pt
USABLE_HEIGHT = PAGE_HEIGHT - MARGIN_TOP - MARGIN_BOTTOM  # 741.89 pt

# Academic Color Palette
COLOR_PRIMARY = colors.HexColor('#0F2A4A')    # Deep Academic Navy
COLOR_SECONDARY = colors.HexColor('#1E56A0')  # Academic Royal Blue
COLOR_DARK = colors.HexColor('#1A1A1A')       # Charcoal Body Text
COLOR_MUTED = colors.HexColor('#4B5563')      # Secondary Slate Grey
COLOR_BORDER = colors.HexColor('#CBD5E1')     # Clean Slate Border
COLOR_LIGHT_BG = colors.HexColor('#F8FAFC')   # Subtle Table/Code Background
COLOR_ACCENT = colors.HexColor('#0284C7')     # Sky Accent


class NumberedCanvas55(canvas.Canvas):
    """
    Two-pass canvas that renders running headers and footers with
    dynamic 'Page X of 55' pagination across all 55 pages.
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
        # Suppress running headers and footers on Page 1 (Title / Bonafide Certificate)
        if self._pageNumber == 1:
            return

        self.saveState()
        
        # --- RUNNING HEADER ---
        self.setFont("Helvetica-Bold", 7.2)
        self.setFillColor(COLOR_PRIMARY)
        self.drawString(
            MARGIN_LEFT,
            PAGE_HEIGHT - 34,
            "CHENNAI INSTITUTE OF TECHNOLOGY  |  DEPT. OF ARTIFICIAL INTELLIGENCE & MACHINE LEARNING"
        )
        self.setFont("Helvetica", 7.2)
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
        self.setFont("Helvetica", 7.2)
        self.setFillColor(COLOR_MUTED)
        self.drawString(
            MARGIN_LEFT,
            32,
            "B.E. (AI & ML) - Project-Based Learning (PBL) Component of Machine Learning"
        )
        self.setFont("Helvetica-Bold", 8.0)
        self.setFillColor(COLOR_PRIMARY)
        self.drawRightString(
            PAGE_WIDTH - MARGIN_RIGHT,
            32,
            f"Page {self._pageNumber} of {page_count}"
        )
        self.restoreState()


def get_styles_55():
    base = getSampleStyleSheet()
    s = {
        'DocTitle': ParagraphStyle('DocTitle', fontName='Helvetica-Bold', fontSize=14, leading=17.5, textColor=COLOR_PRIMARY, alignment=1, spaceAfter=6),
        'DocSubTitle': ParagraphStyle('DocSubTitle', fontName='Helvetica-Bold', fontSize=9.5, leading=13.5, textColor=COLOR_SECONDARY, alignment=1, spaceAfter=6),
        'CoverInstitution': ParagraphStyle('CoverInstitution', fontName='Helvetica-Bold', fontSize=11, leading=15, textColor=COLOR_PRIMARY, alignment=1, spaceAfter=4),
        'CoverDept': ParagraphStyle('CoverDept', fontName='Helvetica-Bold', fontSize=9.5, leading=13.5, textColor=COLOR_SECONDARY, alignment=1, spaceAfter=4),
        'CoverBody': ParagraphStyle('CoverBody', fontName='Times-Roman', fontSize=8.5, leading=11.5, textColor=COLOR_DARK, alignment=1, spaceAfter=3),
        'ChapterHeader': ParagraphStyle('ChapterHeader', fontName='Helvetica-Bold', fontSize=13, leading=16.5, textColor=COLOR_PRIMARY, spaceBefore=2, spaceAfter=2, keepWithNext=True),
        'SectionHeader': ParagraphStyle('SectionHeader', fontName='Helvetica-Bold', fontSize=10.5, leading=13.5, textColor=COLOR_SECONDARY, spaceBefore=4, spaceAfter=2, keepWithNext=True),
        'SubsectionHeader': ParagraphStyle('SubsectionHeader', fontName='Helvetica-Bold', fontSize=9.0, leading=11.8, textColor=COLOR_PRIMARY, spaceBefore=3, spaceAfter=1.5, keepWithNext=True),
        'AcademicBody': ParagraphStyle('AcademicBody', fontName='Times-Roman', fontSize=8.8, leading=11.8, textColor=COLOR_DARK, alignment=4, spaceAfter=3, firstLineIndent=10),
        'AcademicBodyNoIndent': ParagraphStyle('AcademicBodyNoIndent', fontName='Times-Roman', fontSize=8.8, leading=11.8, textColor=COLOR_DARK, alignment=4, spaceAfter=3),
        'BulletItem': ParagraphStyle('BulletItem', fontName='Times-Roman', fontSize=8.5, leading=11.2, textColor=COLOR_DARK, alignment=4, leftIndent=12, firstLineIndent=-8, spaceAfter=2),
        'MathEquation': ParagraphStyle('MathEquation', fontName='Times-Italic', fontSize=8.8, leading=12, textColor=COLOR_PRIMARY, alignment=1, spaceBefore=3, spaceAfter=3),
        'CodeSnippet': ParagraphStyle('CodeSnippet', fontName='Courier', fontSize=7.0, leading=8.8, textColor=colors.HexColor('#1E293B'), spaceBefore=2, spaceAfter=2),
        'TableHeader': ParagraphStyle('TableHeader', fontName='Helvetica-Bold', fontSize=7.5, leading=9.5, textColor=colors.white, alignment=1),
        'TableCell': ParagraphStyle('TableCell', fontName='Times-Roman', fontSize=7.2, leading=9.0, textColor=COLOR_DARK, alignment=0),
        'TableCellCenter': ParagraphStyle('TableCellCenter', fontName='Times-Roman', fontSize=7.2, leading=9.0, textColor=COLOR_DARK, alignment=1),
        'TableCellBold': ParagraphStyle('TableCellBold', fontName='Helvetica-Bold', fontSize=7.2, leading=9.0, textColor=COLOR_PRIMARY, alignment=0),
        'TableCaption': ParagraphStyle('TableCaption', fontName='Helvetica-Bold', fontSize=7.8, leading=10, textColor=COLOR_PRIMARY, alignment=1, spaceBefore=3, spaceAfter=2, keepWithNext=True),
        'FigureCaption': ParagraphStyle('FigureCaption', fontName='Helvetica-Bold', fontSize=7.8, leading=10, textColor=COLOR_PRIMARY, alignment=1, spaceBefore=2, spaceAfter=3),
        'CalloutText': ParagraphStyle('CalloutText', fontName='Times-Italic', fontSize=8.2, leading=11, textColor=COLOR_DARK, spaceBefore=1, spaceAfter=1),
        'ReferenceEntry': ParagraphStyle('ReferenceEntry', fontName='Times-Roman', fontSize=6.8, leading=8.6, textColor=COLOR_DARK, leftIndent=14, firstLineIndent=-14, spaceAfter=1.8),
        # Preliminary Index Styles
        'TOCChapter': ParagraphStyle('TOCChapter', fontName='Helvetica-Bold', fontSize=8.2, leading=10.5, textColor=COLOR_PRIMARY, spaceBefore=2, spaceAfter=1),
        'TOCSection': ParagraphStyle('TOCSection', fontName='Times-Roman', fontSize=7.5, leading=9.5, textColor=COLOR_DARK, leftIndent=12, spaceAfter=0.8),
        'TOCPageNum': ParagraphStyle('TOCPageNum', fontName='Helvetica-Bold', fontSize=7.8, leading=9.5, textColor=COLOR_SECONDARY, alignment=2),
        'IndexEntry': ParagraphStyle('IndexEntry', fontName='Times-Roman', fontSize=7.5, leading=9.8, textColor=COLOR_DARK, spaceAfter=1.5),
        'AbbrKey': ParagraphStyle('AbbrKey', fontName='Helvetica-Bold', fontSize=7.2, leading=9.2, textColor=COLOR_PRIMARY),
        'AbbrVal': ParagraphStyle('AbbrVal', fontName='Times-Roman', fontSize=7.2, leading=9.2, textColor=COLOR_DARK)
    }
    return s


def create_code_block(code_text, styles, width=USABLE_WIDTH):
    p = Paragraph(code_text.replace('\n', '<br/>').replace(' ', '&nbsp;'), styles['CodeSnippet'])
    t = Table([[p]], colWidths=[width])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#F1F5F9')),
        ('BOX', (0, 0), (-1, -1), 0.5, colors.HexColor('#CBD5E1')),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
    ]))
    return t


def create_callout_box(title, text, styles, width=USABLE_WIDTH):
    title_p = Paragraph(f"<b>{title}</b>", styles['SubsectionHeader'])
    body_p = Paragraph(text, styles['CalloutText'])
    t = Table([[title_p], [body_p]], colWidths=[width])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#F0F9FF')),
        ('BOX', (0, 0), (-1, -1), 0.7, colors.HexColor('#0284C7')),
        ('LINEBELOW', (0, 0), (-1, 0), 0.4, colors.HexColor('#BAE6FD')),
        ('TOPPADDING', (0, 0), (-1, -1), 2.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2.5),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
    ]))
    return t
