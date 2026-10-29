"""
ReportLab Styling & NumberedCanvas Configuration for ClearDrive Tech PBL Report
Chennai Institute of Technology (Autonomous) | Department of AI & ML
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph, Spacer, Table, TableStyle, HRFlowable, KeepTogether

# Page Geometry
PAGE_WIDTH, PAGE_HEIGHT = A4
MARGIN_LEFT = 54.0    # 0.75 in (allows binding margin)
MARGIN_RIGHT = 45.0   # ~0.62 in
MARGIN_TOP = 54.0     # 0.75 in
MARGIN_BOTTOM = 54.0  # 0.75 in
USABLE_WIDTH = PAGE_WIDTH - MARGIN_LEFT - MARGIN_RIGHT
USABLE_HEIGHT = PAGE_HEIGHT - MARGIN_TOP - MARGIN_BOTTOM

# Brand Colors (Chennai Institute of Technology & ClearDrive Cyberpunk Theme)
COLOR_PRIMARY = colors.HexColor('#0F2A4A')    # Deep Academic Navy
COLOR_SECONDARY = colors.HexColor('#1E56A0')  # Academic Royal Blue
COLOR_ACCENT = colors.HexColor('#008080')     # Deep Teal
COLOR_DARK = colors.HexColor('#1A1A1A')       # Body Charcoal
COLOR_LIGHT_BG = colors.HexColor('#F8FAFC')   # Clean Slate White
COLOR_BORDER = colors.HexColor('#D1D5DB')     # Subtle Grey Border
COLOR_HIGHLIGHT = colors.HexColor('#D97706')  # Muted Amber for Warnings
COLOR_MUTED = colors.HexColor('#4B5563')      # Secondary text grey


class NumberedCanvas(canvas.Canvas):
    """
    Two-pass canvas that accumulates total page count and renders
    running headers and footers with 'Page X of Y' dynamic pagination.
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
        # Suppress running headers and footers on Page 1 (Cover / Title Page)
        if self._pageNumber == 1:
            return

        self.saveState()
        
        # --- RUNNING HEADER ---
        self.setFont("Helvetica-Bold", 7.5)
        self.setFillColor(COLOR_PRIMARY)
        self.drawString(
            MARGIN_LEFT,
            PAGE_HEIGHT - 36,
            "CHENNAI INSTITUTE OF TECHNOLOGY  |  DEPT. OF ARTIFICIAL INTELLIGENCE & MACHINE LEARNING"
        )
        self.setFont("Helvetica", 7.5)
        self.setFillColor(COLOR_MUTED)
        self.drawRightString(
            PAGE_WIDTH - MARGIN_RIGHT,
            PAGE_HEIGHT - 36,
            "CLEARDRIVE TECH : PBL REPORT"
        )
        
        # Header dividing rule
        self.setStrokeColor(COLOR_BORDER)
        self.setLineWidth(0.6)
        self.line(MARGIN_LEFT, PAGE_HEIGHT - 42, PAGE_WIDTH - MARGIN_RIGHT, PAGE_HEIGHT - 42)

        # --- RUNNING FOOTER ---
        self.line(MARGIN_LEFT, 46, PAGE_WIDTH - MARGIN_RIGHT, 46)
        self.setFont("Helvetica", 7.5)
        self.setFillColor(COLOR_MUTED)
        self.drawString(
            MARGIN_LEFT,
            34,
            "B.E. (AI & ML) — Project-Based Learning (PBL) Component of Machine Learning"
        )
        self.setFont("Helvetica-Bold", 8)
        self.setFillColor(COLOR_PRIMARY)
        self.drawRightString(
            PAGE_WIDTH - MARGIN_RIGHT,
            34,
            f"Page {self._pageNumber} of {page_count}"
        )
        self.restoreState()


def get_report_styles():
    """Builds a cohesive, professional academic typographic hierarchy."""
    base_styles = getSampleStyleSheet()

    custom_styles = {
        'DocTitle': ParagraphStyle(
            'DocTitle',
            parent=base_styles['Title'],
            fontName='Helvetica-Bold',
            fontSize=18,
            leading=23,
            textColor=COLOR_PRIMARY,
            alignment=1, # Centered
            spaceAfter=12
        ),
        'DocSubTitle': ParagraphStyle(
            'DocSubTitle',
            parent=base_styles['Normal'],
            fontName='Helvetica-Bold',
            fontSize=11,
            leading=16,
            textColor=COLOR_SECONDARY,
            alignment=1,
            spaceAfter=15
        ),
        'ChapterHeader': ParagraphStyle(
            'ChapterHeader',
            fontName='Helvetica-Bold',
            fontSize=16,
            leading=20,
            textColor=COLOR_PRIMARY,
            alignment=0, # Left-aligned
            spaceBefore=12,
            spaceAfter=8,
            keepWithNext=True
        ),
        'SectionHeader': ParagraphStyle(
            'SectionHeader',
            fontName='Helvetica-Bold',
            fontSize=12,
            leading=16,
            textColor=COLOR_SECONDARY,
            alignment=0,
            spaceBefore=10,
            spaceAfter=5,
            keepWithNext=True
        ),
        'SubsectionHeader': ParagraphStyle(
            'SubsectionHeader',
            fontName='Helvetica-Bold',
            fontSize=10.5,
            leading=14,
            textColor=COLOR_PRIMARY,
            alignment=0,
            spaceBefore=8,
            spaceAfter=4,
            keepWithNext=True
        ),
        'SubSubsectionHeader': ParagraphStyle(
            'SubSubsectionHeader',
            fontName='Helvetica-Bold',
            fontSize=9.5,
            leading=13,
            textColor=COLOR_MUTED,
            alignment=0,
            spaceBefore=6,
            spaceAfter=3,
            keepWithNext=True
        ),
        'AcademicBody': ParagraphStyle(
            'AcademicBody',
            fontName='Times-Roman',
            fontSize=9.8,
            leading=13.8,
            textColor=COLOR_DARK,
            alignment=4, # Justified
            spaceAfter=6,
            firstLineIndent=14
        ),
        'AcademicBodyNoIndent': ParagraphStyle(
            'AcademicBodyNoIndent',
            fontName='Times-Roman',
            fontSize=9.8,
            leading=13.8,
            textColor=COLOR_DARK,
            alignment=4,
            spaceAfter=6
        ),
        'BulletItem': ParagraphStyle(
            'BulletItem',
            fontName='Times-Roman',
            fontSize=9.5,
            leading=13.2,
            textColor=COLOR_DARK,
            alignment=4,
            leftIndent=16,
            firstLineIndent=-10,
            spaceAfter=4
        ),
        'MathEquation': ParagraphStyle(
            'MathEquation',
            fontName='Times-Italic',
            fontSize=10,
            leading=14,
            textColor=COLOR_PRIMARY,
            alignment=1, # Centered
            spaceBefore=6,
            spaceAfter=6
        ),
        'CodeSnippet': ParagraphStyle(
            'CodeSnippet',
            fontName='Courier',
            fontSize=7.8,
            leading=10.2,
            textColor=colors.HexColor('#1E293B'),
            spaceBefore=3,
            spaceAfter=3
        ),
        'TableHeader': ParagraphStyle(
            'TableHeader',
            fontName='Helvetica-Bold',
            fontSize=8.5,
            leading=11,
            textColor=colors.white,
            alignment=1
        ),
        'TableCell': ParagraphStyle(
            'TableCell',
            fontName='Times-Roman',
            fontSize=8.0,
            leading=10.5,
            textColor=COLOR_DARK,
            alignment=0
        ),
        'TableCellCenter': ParagraphStyle(
            'TableCellCenter',
            fontName='Times-Roman',
            fontSize=8.0,
            leading=10.5,
            textColor=COLOR_DARK,
            alignment=1
        ),
        'TableCellBold': ParagraphStyle(
            'TableCellBold',
            fontName='Helvetica-Bold',
            fontSize=8.0,
            leading=10.5,
            textColor=COLOR_PRIMARY,
            alignment=0
        ),
        'TableCaption': ParagraphStyle(
            'TableCaption',
            fontName='Helvetica-Bold',
            fontSize=8.5,
            leading=12,
            textColor=COLOR_PRIMARY,
            alignment=1,
            spaceBefore=6,
            spaceAfter=4,
            keepWithNext=True
        ),
        'FigureCaption': ParagraphStyle(
            'FigureCaption',
            fontName='Helvetica-Bold',
            fontSize=8.5,
            leading=12,
            textColor=COLOR_PRIMARY,
            alignment=1,
            spaceBefore=4,
            spaceAfter=8
        ),
        'CalloutText': ParagraphStyle(
            'CalloutText',
            fontName='Times-Italic',
            fontSize=9.2,
            leading=13,
            textColor=COLOR_DARK,
            spaceBefore=3,
            spaceAfter=3
        ),
        'ReferenceEntry': ParagraphStyle(
            'ReferenceEntry',
            fontName='Times-Roman',
            fontSize=8.2,
            leading=11.2,
            textColor=COLOR_DARK,
            leftIndent=20,
            firstLineIndent=-20,
            spaceAfter=4
        )
    }

    return custom_styles


def create_code_block(code_text, styles, width=USABLE_WIDTH):
    """Encapsulates code in a styled slate container with subtle border."""
    p = Paragraph(code_text.replace('\n', '<br/>').replace(' ', '&nbsp;'), styles['CodeSnippet'])
    t = Table([[p]], colWidths=[width])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#F1F5F9')),
        ('BOX', (0, 0), (-1, -1), 0.8, colors.HexColor('#CBD5E1')),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
    ]))
    return t


def create_callout_box(title, text, styles, width=USABLE_WIDTH):
    """Renders a formal highlighted note/box."""
    title_p = Paragraph(f"<b>{title}</b>", styles['SubsectionHeader'])
    body_p = Paragraph(text, styles['CalloutText'])
    t = Table([[title_p], [body_p]], colWidths=[width])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#F0F9FF')),
        ('BOX', (0, 0), (-1, -1), 1.0, colors.HexColor('#0284C7')),
        ('LINEBELOW', (0, 0), (-1, 0), 0.5, colors.HexColor('#BAE6FD')),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('LEFTPADDING', (0, 0), (-1, -1), 10),
        ('RIGHTPADDING', (0, 0), (-1, -1), 10),
    ]))
    return t
