import os
import random

def generate_svg(mode):
    if mode == "dark":
        bg_color = "#030712"
        panel_color = "#0F172A"
        border_color = "rgba(255,255,255,0.08)"
        text_color = "#F8FAFC"
        muted_color = "#94A3B8"
        accent_1 = "#7C3AED"
        accent_2 = "#22D3EE"
        accent_3 = "#10B981"
        ascii_color_1 = "#22D3EE"
        ascii_color_2 = "#7C3AED"
        bg_glow_1 = "rgba(34, 211, 238, 0.15)"
        bg_glow_2 = "rgba(124, 58, 237, 0.15)"
        bg_glow_3 = "rgba(16, 185, 129, 0.15)"
    else:
        bg_color = "#FFFFFF"
        panel_color = "#F8FAFC"
        border_color = "rgba(15,23,42,0.08)"
        text_color = "#0F172A"
        muted_color = "#475569"
        accent_1 = "#2563EB"
        accent_2 = "#06B6D4"
        accent_3 = "#10B981"
        ascii_color_1 = "#2563EB"
        ascii_color_2 = "#06B6D4"
        bg_glow_1 = "rgba(37, 99, 235, 0.1)"
        bg_glow_2 = "rgba(6, 182, 212, 0.1)"
        bg_glow_3 = "rgba(16, 185, 129, 0.1)"
        
    width = 1180
    height = 610

    # Skills
    skills = ["Python", "C++", "Next.js", "Flutter", "Node.js", "LLaMA 3", "Firebase", "GCP", "MATLAB", "Docker", "Dart"]

    # ASCII portrait lines
    ascii_art = [
        "      .::::::::...      ",
        "    .::::::::::::::::.    ",
        "  .::::::::::::::::::::.  ",
        " .::::::::::::::::::::::. ",
        " :::::::::::::::::::::::: ",
        " :::::::::::::::::::::::: ",
        " :::::::::::::::::::::::: ",
        " `::::::::::::::::::::::' ",
        "  `::::::::::::::::::::'  ",
        "    `::::::::::::::::'    ",
        "      `'::::::::::'`      ",
        "          ......          ",
        "      .::::::::::::.      ",
        "    .::::::::::::::::.    ",
        "  .::::::::::::::::::::.  "
    ]

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
    <defs>
        <!-- Gradients -->
        <linearGradient id="accent-gradient" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="{accent_1}">
                <animate attributeName="stop-color" values="{accent_1};{accent_2};{accent_3};{accent_1}" dur="8s" repeatCount="indefinite" />
            </stop>
            <stop offset="50%" stop-color="{accent_2}">
                <animate attributeName="stop-color" values="{accent_2};{accent_3};{accent_1};{accent_2}" dur="8s" repeatCount="indefinite" />
            </stop>
            <stop offset="100%" stop-color="{accent_3}">
                <animate attributeName="stop-color" values="{accent_3};{accent_1};{accent_2};{accent_3}" dur="8s" repeatCount="indefinite" />
            </stop>
        </linearGradient>

        <linearGradient id="ascii-gradient" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="{ascii_color_1}">
                <animate attributeName="stop-color" values="{ascii_color_1};{ascii_color_2};{ascii_color_1}" dur="5s" repeatCount="indefinite" />
            </stop>
            <stop offset="100%" stop-color="{ascii_color_2}">
                <animate attributeName="stop-color" values="{ascii_color_2};{ascii_color_1};{ascii_color_2}" dur="5s" repeatCount="indefinite" />
            </stop>
        </linearGradient>

        <!-- Filters -->
        <filter id="glow">
            <feGaussianBlur stdDeviation="4" result="coloredBlur"/>
            <feMerge>
                <feMergeNode in="coloredBlur"/>
                <feMergeNode in="SourceGraphic"/>
            </feMerge>
        </filter>
        
        <filter id="soft-glow">
            <feGaussianBlur stdDeviation="2" result="coloredBlur"/>
            <feMerge>
                <feMergeNode in="coloredBlur"/>
                <feMergeNode in="SourceGraphic"/>
            </feMerge>
        </filter>
        
        <filter id="blur-bg">
            <feGaussianBlur stdDeviation="30"/>
        </filter>
        
        <!-- Noise filter removed for GitHub compatibility -->
        
        <!-- Clip Paths -->
        <clipPath id="typing-clip">
            <rect x="0" y="-30" width="0" height="60">
                <animate attributeName="width" values="0;278;278;0;0;451;451;0;0;566;566;0;0" keyTimes="0;0.05;0.25;0.3;0.333;0.383;0.583;0.633;0.666;0.716;0.916;0.966;1" dur="15s" repeatCount="indefinite" />
            </rect>
        </clipPath>

        <clipPath id="reveal-clip">
            <rect x="0" y="0" width="0" height="1000">
                <animate attributeName="width" values="0;1000" dur="2s" fill="freeze" begin="0.5s"/>
            </rect>
        </clipPath>

    </defs>

    <!-- Background -->
    <rect width="{width}" height="{height}" fill="{bg_color}" rx="24"/>
    
    <!-- Floating radial gradients -->
    <circle cx="200" cy="150" r="200" fill="{bg_glow_1}" filter="url(#blur-bg)">
        <animateMotion path="M 0,0 a 80,80 0 1,0 160,0 a 80,80 0 1,0 -160,0" dur="15s" repeatCount="indefinite" />
    </circle>
    <circle cx="900" cy="450" r="250" fill="{bg_glow_2}" filter="url(#blur-bg)">
        <animateMotion path="M 0,0 a -90,90 0 1,0 180,0 a -90,90 0 1,0 -180,0" dur="20s" repeatCount="indefinite" />
    </circle>
    <circle cx="600" cy="100" r="220" fill="{bg_glow_3}" filter="url(#blur-bg)">
        <animateMotion path="M 0,0 a 70,70 0 1,1 140,0 a 70,70 0 1,1 -140,0" dur="18s" repeatCount="indefinite" />
    </circle>


    <!-- Particles -->
"""
    # Fix random seed so the animation feels consistent
    random.seed(42)
    for _ in range(25):
        px = random.randint(50, width - 50)
        py = random.randint(50, height - 50)
        r = random.uniform(1.0, 2.5)
        dur = random.uniform(4, 9)
        svg += f'    <circle cx="{px}" cy="{py}" r="{r}" fill="{text_color}" opacity="0">\n'
        svg += f'        <animate attributeName="opacity" values="0;0.6;0" dur="{dur}s" repeatCount="indefinite" />\n'
        svg += f'        <animate attributeName="cy" values="{py};{py-40};{py}" dur="{dur*1.5}s" repeatCount="indefinite" />\n'
        svg += '    </circle>\n'

    svg += f"""
    <!-- Left Side: ASCII Portrait -->
    <g transform="translate(40, 30)">
        <!-- Glass Panel -->
        <rect width="420" height="550" fill="{panel_color}" rx="16" fill-opacity="0.7" stroke="{border_color}" stroke-width="1.5">
            <animate attributeName="stroke" values="{border_color};{bg_glow_1};{border_color}" dur="4s" repeatCount="indefinite" />
        </rect>
        
        <!-- Border Shimmer -->
        <rect width="420" height="550" fill="none" rx="16" stroke="url(#accent-gradient)" stroke-width="2" opacity="0" stroke-dasharray="20 400" stroke-dashoffset="0">
            <animate attributeName="opacity" values="0;1;0" dur="6s" repeatCount="indefinite" />
            <animate attributeName="stroke-dashoffset" values="0;-420" dur="6s" repeatCount="indefinite" />
        </rect>

        <!-- Inner content floating -->
        <g>
            <animateTransform attributeName="transform" type="translate" values="0,0; 0,-10; 0,0" dur="6s" repeatCount="indefinite" />
            
            <text font-family="monospace" font-size="16" font-weight="bold" fill="url(#ascii-gradient)" filter="url(#glow)" x="210" y="100" text-anchor="middle" clip-path="url(#reveal-clip)">
"""
    y_offset = 120
    for idx, line in enumerate(ascii_art):
        begin_time = idx * 0.1
        # &#160; for spaces
        safe_line = line.replace(" ", "&#160;")
        svg += f'                <tspan x="210" y="{y_offset}" opacity="0"><animate attributeName="opacity" values="0;1" dur="0.1s" begin="{begin_time}s" fill="freeze" />{safe_line}</tspan>\n'
        y_offset += 20
        
    svg += f"""            </text>
            
            <!-- Moving scanline -->
            <rect x="20" y="10" width="380" height="3" fill="url(#ascii-gradient)" opacity="0" filter="url(#glow)">
                <animate attributeName="opacity" values="0;0.5;0" dur="8s" repeatCount="indefinite" />
                <animate attributeName="y" values="10;540;10" dur="8s" repeatCount="indefinite" />
            </rect>
            
        </g>
    </g>

    <!-- Right Side: Terminal Window -->
    <g transform="translate(490, 30)">
        <!-- Glass Panel -->
        <rect width="650" height="550" fill="{panel_color}" rx="16" fill-opacity="0.7" stroke="{border_color}" stroke-width="1.5" />
        
        <!-- Terminal Header -->
        <rect width="650" height="40" fill="{border_color}" rx="16" />
        <rect width="650" height="20" y="20" fill="{border_color}" />
        <circle cx="30" cy="20" r="6" fill="#EF4444" />
        <circle cx="50" cy="20" r="6" fill="#F59E0B" />
        <circle cx="70" cy="20" r="6" fill="#10B981" />
        <text x="325" y="25" fill="{muted_color}" font-family="monospace" font-size="12" text-anchor="middle">~ / developer / profile</text>

        <!-- Content -->
        <g transform="translate(40, 80)">
            <g clip-path="url(#reveal-clip)">
                <!-- Greeting -->
                <text x="0" y="30" fill="{text_color}" font-family="system-ui, -apple-system, sans-serif" font-size="36" font-weight="bold">
                    Hi 👋 I'm Shlok Noval
                </text>
                
                <!-- Animated Typing Text -->
                <g transform="translate(0, 75)">
                    <g clip-path="url(#typing-clip)">
                        <text x="0" y="0" fill="url(#accent-gradient)" font-family="monospace" font-size="24" font-weight="bold">
                            <animate attributeName="opacity" values="1;1;0;0;0;0" keyTimes="0;0.3;0.3;0.633;0.633;1" dur="15s" repeatCount="indefinite" />
                            &gt; 6x Hackathon Winner
                        </text>
                        <text x="0" y="0" fill="url(#accent-gradient)" font-family="monospace" font-size="24" font-weight="bold" opacity="0">
                            <animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="0;0.3;0.3;0.633;0.633;1" dur="15s" repeatCount="indefinite" />
                            &gt; Building Scalable AIML Projects
                        </text>
                        <text x="0" y="0" fill="url(#accent-gradient)" font-family="monospace" font-size="24" font-weight="bold" opacity="0">
                            <animate attributeName="opacity" values="0;0;1;1" keyTimes="0;0.633;0.633;1" dur="15s" repeatCount="indefinite" />
                            &gt; Full stack and AIML freelance developer
                        </text>
                    </g>
                    <!-- Blinking Cursor -->
                    <rect x="0" y="-22" width="12" height="26" fill="url(#accent-gradient)">
                        <animate attributeName="opacity" values="1;0;1" dur="0.8s" repeatCount="indefinite" />
                        <animate attributeName="x" values="24;302;302;24;24;475;475;24;24;590;590;24;24" keyTimes="0;0.05;0.25;0.3;0.333;0.383;0.583;0.633;0.666;0.716;0.916;0.966;1" dur="15s" repeatCount="indefinite" />
                    </rect>
                </g>

                <!-- Personal Info -->
                <g transform="translate(0, 140)" font-family="monospace" font-size="16" fill="{muted_color}">
                    <text x="0" y="0" opacity="0"><animate attributeName="opacity" values="0;1" dur="0.5s" begin="1s" fill="freeze" /><tspan fill="{accent_2}">const</tspan> location = <tspan fill="{text_color}">"Chh. Sambhajinagar (M.H.), India"</tspan>;</text>
                    <text x="0" y="28" opacity="0"><animate attributeName="opacity" values="0;1" dur="0.5s" begin="1.2s" fill="freeze" /><tspan fill="{accent_2}">const</tspan> education = <tspan fill="{text_color}">"Computer Science"</tspan>;</text>
                    <text x="0" y="56" opacity="0"><animate attributeName="opacity" values="0;1" dur="0.5s" begin="1.4s" fill="freeze" /><tspan fill="{accent_2}">const</tspan> focus = <tspan fill="{text_color}">"Building Scalable &amp; Production-level Apps"</tspan>;</text>
                    <text x="0" y="84" opacity="0"><animate attributeName="opacity" values="0;1" dur="0.5s" begin="1.6s" fill="freeze" /><tspan fill="{accent_2}">const</tspan> email = <tspan fill="{text_color}">"shloktechnical@gmail.com"</tspan>;</text>
                </g>

                <!-- Skills Section -->
                <g transform="translate(0, 270)">
                    <text x="0" y="0" fill="{text_color}" font-family="system-ui, -apple-system, sans-serif" font-size="18" font-weight="600" opacity="0">
                        <animate attributeName="opacity" values="0;1" dur="0.5s" begin="2s" fill="freeze" />
                        Skills
                    </text>
                    
                    <g transform="translate(0, 20)">
"""
    
    # Glowing pills for skills
    sx, sy = 0, 0
    delay = 2.2
    for skill in skills:
        pill_width = len(skill) * 9 + 30
        if sx + pill_width > 570:
            sx = 0
            sy += 45
            
        svg += f"""
                        <g transform="translate({sx}, {sy})" opacity="0">
                            <animate attributeName="opacity" values="0;1" dur="0.5s" begin="{delay}s" fill="freeze" />
                            <animateTransform attributeName="transform" type="translate" values="{sx},{sy+10}; {sx},{sy}" dur="0.5s" begin="{delay}s" fill="freeze" />
                            <rect width="{pill_width}" height="32" rx="16" fill="{border_color}" stroke="url(#accent-gradient)" stroke-width="1" />
                            <text x="{pill_width/2}" y="21" fill="{text_color}" font-family="system-ui, -apple-system, sans-serif" font-size="14" text-anchor="middle">{skill}</text>
                            
                            <rect width="{pill_width}" height="32" rx="16" fill="url(#accent-gradient)" opacity="0" filter="url(#glow)">
                                <animate attributeName="opacity" values="0; 0.2; 0" dur="{random.uniform(4, 7)}s" begin="{delay}s" repeatCount="indefinite" />
                            </rect>
                        </g>
"""
        sx += pill_width + 12
        delay += 0.1

    svg += f"""
                    </g>
                </g>

            </g>
        </g>
    </g>

    </svg>"""
    return svg

with open("dark.svg", "w", encoding="utf-8") as f:
    f.write(generate_svg("dark"))
    
with open("light.svg", "w", encoding="utf-8") as f:
    f.write(generate_svg("light"))
