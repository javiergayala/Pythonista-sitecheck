import ui
import requests

w, h = ui.get_screen_size()

# fonts
APPFONT = 'HelveticaNeue-Thin'
APPFONT_BOLD = 'HelveticaNeue'
CONSOLEFONT = 'SourceCodePro-Medium'

# colors
GREEN = '#4CD964'
RED = '#FF3B30'
BLUE = '#007AFF'
LTBLUE = '#5AC8FA'
ORANGE = '#FF9500'
YELLOW = '#FFCC00'
GRAY0 = '#EFEFF4'
GRAY1 = '#CECED2'
GRAY2 = '#8E8E93'
WHITE = '#FFFFFF'
BLACK = '#000000'

# font sizes
H1 = 30
H2 = 20
T1 = 16
T12 = 12

# padding
PAD = 10

v = None
r = None
sess = None
usrHdrs = None
url = None


v = ui.load_view()

# boilerplate
startingTxt = '''
HeaderView

Your website's headers will be displayed in this box.
'''
startingHtml = '''
<!DOCTYPE html>
<html>
<head>
<style>
body {
  background-color: '#CECED2';
  font-family: 'HelveticaNeue';
  padding: 1em;
}
.alert {color: #FF3B30;}
.green {color: #4CD964;}
</style>
</head>
<body>
<h1>WebView</h1>
<p>Your website will be rendered in this box.</p>
</body>
</html>
'''


def compileHeaders(headerName=None, headerVal=None):
    """
    >>> compileHeaders('Host', 'www.domain.com')
    {'Host': 'www.domain.com'}
    """
    usrHdrs = None
    if headerName != '':
        usrHdrs = {}
        usrHdrs[headerName] = headerVal
    return usrHdrs


def textfield_should_return(textfield=None):
    textfield.end_editing()
    return True


def openreq(url=url):
    sess = requests.Session()
    headers = compileHeaders(v['headerName'].text, v['headerVal'].text)
    return sess.get(url, headers=headers,
                    allow_redirects=v['redirectsSwitch'].value)


def button_tapped(sender, v=v, r=None, sess=sess):
    if r is None:
        r = openreq(v['urlField'].text)
    textdump = "Status Code: %s\n" % r.status_code
    for k, val in list(r.headers.items()):
        textdump += "%s: %s\n" % (k, val)
    v['hdrView'].text = textdump
    v['siteView'].load_html(r.content.decode())
    r = None


# header label
hdr = ui.Label()
hdr.name = 'hdrLabel'
hdr.text = 'Site Checker'
hdr.font = (APPFONT, H1)
hdr.width = w/2
hdr.height = H1 + H1/2
hdr.center = (w/2, H1)
hdr.alignment = ui.ALIGN_CENTER
hdr.text_color = BLUE
y1 = hdr.y + hdr.height

# Site Label
urlHdr = ui.Label()
urlHdr.name = 'urlHdr'
urlHdr.text = 'Site:'
urlHdr.font = (APPFONT, H2)
urlHdr.frame = (PAD, y1, w - PAD * 2, H2 + H2/2)
y2 = urlHdr.y + urlHdr.height + PAD

# URL Text Field
urlField = ui.TextField()
urlField.name = 'urlField'
urlField.placeholder = 'Enter URL Here'
urlField.autocapitalization_type = ui.AUTOCAPITALIZE_NONE
urlField.autocorrection_type = False
urlField.clear_button_mode = 'while_editing'
urlField.keyboard_type = ui.KEYBOARD_URL
urlField.spellchecking_type = False
urlField.font = (CONSOLEFONT, T1)
urlField.height = T1 + T1/2
urlField.frame = (PAD, y2, w - PAD * 2, urlField.height)
y3 = urlField.y + urlField.height + PAD

# Headers Label
headerHdr = ui.Label()
headerHdr.name = 'headersLbl'
headerHdr.text = 'Headers:'
headerHdr.font = (APPFONT, H2)
headerHdr.frame = (PAD, y3, w - PAD * 2, H2 + H2 / 2)
y4 = headerHdr.y + headerHdr.height + PAD

# Headers Fields
headerName = ui.TextField()
headerName.placeholder = 'Header'
headerName.name = 'headerName'
headerName.autocorrection_type = False
headerName.clear_button_mode = 'while_editing'
headerName.keyboard_type = ui.KEYBOARD_DEFAULT
headerName.spellchecking_type = False
headerName.font = (CONSOLEFONT, T1)
headerName.height = T1 + T1/2
headerName.frame = (PAD, y4, (w - PAD * 2)/2, headerName.height)
headerVal = ui.TextField()
headerVal.name = 'headerVal'
headerVal.placeholder = 'Value'
headerVal.autocorrection_type = False
headerVal.autocapitalization_type = ui.AUTOCAPITALIZE_NONE
headerVal.clear_button_mode = 'while_editing'
headerVal.keyboard_type = ui.KEYBOARD_DEFAULT
headerVal.spellchecking_type = False
headerVal.font = (CONSOLEFONT, T1)
headerVal.height = headerName.height
headerVal.frame = ((w / 2) + PAD, y4, (w - PAD * 2)/2 - PAD, headerVal.height)
y5 = headerName.y + headerName.height + PAD

# Follow Redirects
redirectsLbl = ui.Label()
redirectsLbl.name = 'redirectsLbl'
redirectsLbl.text = 'Follow Redirects'
redirectsLbl.alignment = ui.ALIGN_RIGHT
redirectsLbl.font = (APPFONT, T1)
redirectsLbl.height = T1 + T1/2
redirectsLbl.frame = (PAD, y5, (w - PAD * 2)/2, redirectsLbl.height)
redirectsSwitch = ui.Switch()
redirectsSwitch.name = 'redirectsSwitch'
redirectsSwitch.value = True
redirectsSwitch.frame = ((w / 2) + PAD, y5, (w - PAD * 2)/2,
                         redirectsSwitch.height)
y6 = redirectsLbl.y + redirectsSwitch.height + PAD

# Submit Button
goBtn = ui.Button(title='Submit')
goBtn.name = 'goBtn'
goBtn.font = (APPFONT_BOLD, H2)
goBtn.background_color = GREEN
goBtn.tint_color = WHITE
goBtn.corner_radius = 5
goBtn.height = H2 + H2/2
goBtn.width = w/4
goBtn.center = (w/2, y6)
goBtn.frame = (w/2 - goBtn.width/2, y6, goBtn.width, goBtn.height)
goBtn.enabled = True
y7 = goBtn.y + goBtn.height + PAD

# Headers Text View
hdrView = ui.TextView()
hdrView.name = 'hdrView'
hdrView.height = h/6
hdrView.frame = (PAD, y7, w - PAD * 2, hdrView.height)
hdrView.border_color = GRAY2
hdrView.border_width = 1
hdrView.font = (CONSOLEFONT, T12)
hdrView.text = startingTxt
y8 = hdrView.y + hdrView.height + PAD

# Site View
siteView = ui.WebView()
siteView.name = 'siteView'
siteView.height = h/6
siteView.flex = ''
siteView.frame = (PAD, y8, w - PAD * 2, v.height - 30)
siteView.border_color = GRAY2
siteView.border_width = 1
siteView.load_html(startingHtml)
y9 = siteView.y + siteView.height + PAD

# Footer Label
footer = ui.Label()
footer.name = 'Footer'
footer.text = '© 2016 Javier Ayala All Rights Reserved'
footer.font = (APPFONT, T12)
footer.flex = 'WB'
footer.frame = (v.width/2,
                h - (footer.height * 1.25),
                (w - PAD * 2) / 2,
                footer.height)

# Load and present the UI
sections = [hdr, urlHdr, urlField, headerHdr, headerName, headerVal,
            redirectsLbl, redirectsSwitch, goBtn, hdrView, siteView, footer]

textentry_fields = ['urlField', 'headerName', 'headerVal']


for i in sections:
    v.add_subview(i)

for t in textentry_fields:
    v[t].action = textfield_should_return
v['goBtn'].action = button_tapped
v.present('sheet')
v.flex = 'H'
