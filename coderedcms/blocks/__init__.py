"""
Blocks module entry point. Used to cleanly organize blocks into
individual files based on purpose, but provide them all as a
single `blocks` module.
"""

from django.utils.translation import ugettext_lazy as _
from wagtail.core.blocks import CharBlock, StreamBlock, StructBlock

from coderedcms.wagtail_flexible_forms.blocks import FormStepBlock, FormStepsBlock

from .stream_form_blocks import * #noqa
from .base_blocks import * #noqa
from .html_blocks import * #noqa
from .metadata_blocks import * #noqa
from .content_blocks import * #noqa
from .layout_blocks import * #noqa



# Collections of blocks commonly used together.

HTML_STREAMBLOCKS = [
    ('text', RichTextBlock(icon='fa-file-text-o')),
    ('button', ButtonBlock()),
    ('image', ImageBlock()),
    ('image_link', ImageLinkBlock()),
    ('html', blocks.RawHTMLBlock(icon='code', classname='monospace', label=_('HTML'), )),
    ('download', DownloadBlock()),
    ('embed_video', EmbedVideoBlock()),
    ('quote', QuoteBlock()),
    ('table', TableBlock()),
    ('google_map', EmbedGoogleMapBlock()),
    ('page_list', PageListBlock()),
    ('page_preview', PagePreviewBlock()),
]

CONTENT_STREAMBLOCKS = HTML_STREAMBLOCKS + [
    ('card', CardBlock()),
    ('carousel', CarouselBlock()),
    ('image_gallery', ImageGalleryBlock()),
    ('modal', ModalBlock(HTML_STREAMBLOCKS)),
    ('pricelist', PriceListBlock()),
    ('reusable_content', ReusableContentBlock()),
]

NAVIGATION_STREAMBLOCKS = [
    ('page_link', NavPageLinkWithSubLinkBlock()),
    ('external_link', NavExternalLinkWithSubLinkBlock()),
    ('document_link', NavDocumentLinkWithSubLinkBlock()),
]

BASIC_LAYOUT_STREAMBLOCKS = [
    ('row', GridBlock(HTML_STREAMBLOCKS)),
    ('html', blocks.RawHTMLBlock(icon='code', classname='monospace', label=_('HTML'))),
]

LAYOUT_STREAMBLOCKS = [
    ('hero', HeroBlock([
        ('row', GridBlock(CONTENT_STREAMBLOCKS)),
        ('cardgrid', CardGridBlock([
            ('card', CardBlock()),])
        ),
        ('html', blocks.RawHTMLBlock(icon='code', classname='monospace', label=_('HTML'))),])
    ),
    ('row', GridBlock(CONTENT_STREAMBLOCKS)),
    ('cardgrid', CardGridBlock([
        ('card', CardBlock()),])
    ),
    ('html', blocks.RawHTMLBlock(icon='code', classname='monospace', label=_('HTML'))),
]

STREAMFORM_FIELDBLOCKS = [
    ('sf_singleline', CoderedStreamFormCharFieldBlock(group=_('Fields'))),
    ('sf_multiline', CoderedStreamFormTextFieldBlock(group=_('Fields'))),
    ('sf_number', CoderedStreamFormNumberFieldBlock(group=_('Fields'))),
    ('sf_checkboxes', CoderedStreamFormCheckboxesFieldBlock(group=_('Fields'))),
    ('sf_radios', CoderedStreamFormRadioButtonsFieldBlock(group=_('Fields'))),
    ('sf_dropdown', CoderedStreamFormDropdownFieldBlock(group=_('Fields'))),
    ('sf_checkbox', CoderedStreamFormCheckboxFieldBlock(group=_('Fields'))),
    ('sf_date', CoderedStreamFormDateFieldBlock(group=_('Fields'))),
    ('sf_time', CoderedStreamFormTimeFieldBlock(group=_('Fields'))),
    ('sf_datetime', CoderedStreamFormDateTimeFieldBlock(group=_('Fields'))),
    ('sf_image', CoderedStreamFormImageFieldBlock(group=_('Fields'))),
    ('sf_file', CoderedStreamFormFileFieldBlock(group=_('Fields'))),
]

STREAMFORM_BLOCKS = [
    ('step', CoderedStreamFormStepBlock(STREAMFORM_FIELDBLOCKS + HTML_STREAMBLOCKS)),
]
