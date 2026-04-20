from Cocoa import NSWindow, NSScreen, NSWindowStyleMaskBorderless, NSBackingStoreBuffered, NSColor, NSStatusWindowLevel

class OverlayWindow(NSWindow):
    def init(self):
        screen_frame = NSScreen.mainScreen().frame()

        self = NSWindow.initWithContentRect_styleMask_backing_defer_(
            self,
            screen_frame,
            NSWindowStyleMaskBorderless,
            NSBackingStoreBuffered,
            False
        )

        if self:
            self.setOpaque_(False)
            self.setBackgroundColor_(NSColor.clearColor())
            self.setLevel_(NSStatusWindowLevel)
            self.setIgnoresMouseEvents_(True)

        return self
    
class Overlay:
    def __init__(self, window, font):
        self.window = window
        self.labels = []
        self.font = font

    def clear(self):
        for l in self.labels:
            l.removeFromSuperview()
        self.labels = []

    def draw_text(self, x, y, text):
        from Cocoa import NSTextField, NSFont

        label = NSTextField.alloc().initWithFrame_(((x, y), (400, 30)))

        label.setStringValue_(text)
        label.setBezeled_(False)
        label.setDrawsBackground_(False)
        label.setEditable_(False)
        label.setSelectable_(False)

        label.setTextColor_(NSColor.whiteColor())
        label.setFont_(self.font)

        self.window.contentView().addSubview_(label)
        self.labels.append(label)