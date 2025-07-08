import { Orbitron } from "next/font/google"
import "./globals.css"

// Note this configuration is important for th fonts to wor
const orbitron = Orbitron({
  subsets: ["latin"],
  variable: "--font-orbitron",
  display: "swap", // optional but recommended
  weight: ["400", "700"], // optional: specify weights you need
})

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode
}>) {
  return (
    <html lang="en">
      <body className={`${orbitron.className} antialiased`}>{children}</body>
    </html>
  )
}
