import re

translations = {
    "Advanced Click Actions": "Ações Avançadas de Clique",
    "Ctrl+Click Command:": "Comando Ctrl+Clique:",
    "Middle Click Command:": "Comando Clique do Meio:",
    "Shift+Click Command:": "Comando Shift+Clique:",
    "Alt+Click Command:": "Comando Alt+Clique:",
    "Advanced Mouse Wheel Actions": "Ações Avançadas da Roda do Mouse",
    "Ctrl+Scroll Cooldown:": "Intervalo de Ctrl+Rolagem:",
    "Ctrl+Scroll Up:": "Ctrl+Rolar para Cima:",
    "Ctrl+Scroll Down:": "Ctrl+Rolar para Baixo:",
    "Long Press Color:": "Cor de clique longo:",
    "Click Command:": "Comando de clique:",
    "Long Press Command:": "Comando de clique longo:",
    "Peek": "Espiar",
    "Show desktop on hover:": "Mostrar área de trabalho ao passar o mouse:",
    "Peek threshold:": "Tempo de espera (ms):",
    "Unlock Widgets": "Desbloquear Widgets",
    "Lock Widgets": "Bloquear Widgets",
    "Select a Bash Script (.sh)": "Selecione um script Bash (.sh)",
    "Select Script": "Selecionar Script",
    "Command": "Comando",
    "Display:": "Exibição:",
    "Use Emoji/Icon instead of colors": "Usar Emoji/Ícone em vez de cores",
    "Icon / Emoji:": "Ícone / Emoji:",
    "--- Gerenciamento de Janelas e Telas ---": "--- Gerenciamento de Janelas e Telas ---",
    "Overview": "Visão Geral",
    "Present Windows (Current Desktop)": "Apresentar Janelas (Área Atual)",
    "Present Windows (All Desktops)": "Apresentar Janelas (Todas)",
    "Present Windows (Window Class)": "Apresentar Janelas (Por Classe)",
    "Show Desktop Grid": "Mostrar Grade de Áreas de Trabalho",
    "--- Alternância de Áreas de Trabalho ---": "--- Alternância de Áreas de Trabalho ---",
    "Switch Desktop Right": "Mudar Área de Trabalho Direita",
    "Switch Desktop Left": "Mudar Área de Trabalho Esquerda",
    "Window to Next Desktop": "Mover Janela para Próxima Área",
    "Window to Prev Desktop": "Mover Janela para Área Anterior",
    "Window to Next Screen": "Mover Janela para Próxima Tela",
    "Window to Prev Screen": "Mover Janela para Tela Anterior",
    "--- Posicionamento e Tiling ---": "--- Posicionamento e Tiling ---",
    "Edit Tiles": "Editar Ladrilhos",
    "Switch Window Left": "Alternar Janela à Esquerda",
    "Switch Window Right": "Alternar Janela à Direita",
    "Switch Window Up": "Alternar Janela Acima",
    "Switch Window Down": "Alternar Janela Abaixo",
    "Window Move Center": "Mover Janela para o Centro",
    "Quick Tile Left": "Anexar Janela à Esquerda",
    "Quick Tile Right": "Anexar Janela à Direita",
    "Quick Tile Top": "Anexar Janela ao Topo",
    "Quick Tile Bottom": "Anexar Janela à Base",
    "Quick Tile Top Left": "Anexar Janela Topo-Esquerda",
    "Quick Tile Top Right": "Anexar Janela Topo-Direita",
    "Quick Tile Bottom Left": "Anexar Janela Base-Esquerda",
    "Quick Tile Bottom Right": "Anexar Janela Base-Direita",
    "Pack Window Left": "Empacotar Janela à Esquerda",
    "Pack Window Right": "Empacotar Janela à Direita",
    "Pack Window Up": "Empacotar Janela Acima",
    "Pack Window Down": "Empacotar Janela Abaixo",
    "--- Áudio (amixer / Sem UI) ---": "--- Áudio (amixer / Sem UI) ---",
    "Volume Up (amixer)": "Aumentar Volume (amixer)",
    "Volume Down (amixer)": "Diminuir Volume (amixer)",
    "--- Áudio (kmix) ---": "--- Áudio (kmix) ---",
    "Mute/Unmute": "Mutar/Desmutar",
    "Volume Up": "Aumentar Volume",
    "Volume Down": "Diminuir Volume",
    "Mic Mute": "Mutar Microfone",
    "--- Controle de Mídia ---": "--- Controle de Mídia ---",
    "Play/Pause": "Tocar/Pausar",
    "Next Track": "Próxima Faixa",
    "Prev Track": "Faixa Anterior",
    "Peek at Desktop": "Espiar Área de Trabalho",
    "Stop Peeking at Desktop": "Parar de Espiar",
    "Moves windows back to their original positions": "Mover janelas para a posição original",
    "Temporarily shows the desktop by moving windows away": "Exibe a área de trabalho temporariamente",
    "Restore All Minimized Windows": "Restaurar Janelas Minimizadas",
    "Minimize All Windows": "Minimizar Todas Janelas",
    "Restores the previously minimized windows": "Restaura janelas previamente minimizadas",
    "Shows the Desktop by minimizing all windows": "Exibe a área de trabalho minimizando as janelas",
    "Run custom command": "Executar comando personalizado",
    "Run user-defined command when pressed": "Executa comando definido pelo usuário",
    "Show Desktop": "Exibir a Área de Trabalho",
    "Run Command": "Executar comando"
}

with open("translate/pt_BR.po", "r") as f:
    content = f.read()

# Remove fuzzy tags
content = re.sub(r"#, fuzzy\n", "", content)

# Inject translations
for eng, pt in translations.items():
    pattern = r'msgid "' + re.escape(eng) + r'"\nmsgstr ".*?"'
    replacement = 'msgid "' + eng + '"\nmsgstr "' + pt + '"'
    content = re.sub(pattern, replacement, content)

with open("translate/pt_BR.po", "w") as f:
    f.write(content)

print("pt_BR.po updated!")
