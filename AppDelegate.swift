import Cocoa

class AppDelegate: NSObject, NSApplicationDelegate {
    
    var blurWindow: NSWindow?

    // Uygulama arka plana veya Mission Control'e geçtiğinde çalışır
    func applicationWillResignActive(_ notification: Notification) {
        if let mainWindow = NSApplication.shared.mainWindow {
            let visualEffect = NSVisualEffectView(frame: mainWindow.contentView!.bounds)
            visualEffect.blendingMode = .withinWindow
            visualEffect.material = .hudWindow
            visualEffect.state = .active
            visualEffect.identifier = NSUserInterfaceItemIdentifier("SecurityBlur")
            
            mainWindow.contentView?.addSubview(visualEffect)
        }
    }

    // Uygulama tekrar aktif olduğunda çalışır (Bulanıklığı kaldırır)
    func applicationDidBecomeActive(_ notification: Notification) {
        if let mainWindow = NSApplication.shared.mainWindow {
            mainWindow.contentView?.subviews.removeAll(where: { $0.identifier?.rawValue == "SecurityBlur" })
        }
    }
}
