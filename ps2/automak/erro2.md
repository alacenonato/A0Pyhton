Perfeito! Agora tenho todas as informações que precisava.

Vou traduzir as configurações do seu OPL para o formato que o POPStarter entende.

---

## 📝 Suas configurações atuais (OPL)

| Item | Valor |
|------|-------|
| IP do PS2 | `192.168.25.200` |
| Mask | `255.255.255.0` |
| Gateway | `192.168.25.1` |
| Servidor | `GVT-GATEWAY` (NetBIOS) |
| Porta | `445` |
| Compartilhamento | `Drive1_1` |
| Usuário | `guest` |
| Senha | (vazia) |

---

## ⚠️ Problema identificado

O POPStarter **não resolve nomes NetBIOS** como `GVT-GATEWAY`. Ele precisa do **endereço IP numérico** do servidor.

Você precisa descobrir o IP do `GVT-GATEWAY`. Provavelmente é `192.168.25.1` (o mesmo do Gateway), mas vamos confirmar.

---

## 🔍 Passo 1: Descobrir o IP do servidor

No seu computador Linux (que está compartilhando os jogos), execute:

```bash
ip addr show
```

ou

```bash
hostname -I
```

Anote o IP que aparece (ex: `192.168.25.100` ou similar).

**Importante:** O IP do servidor precisa ser **fixo** e estar na mesma rede do PS2 (começando com `192.168.25.x`).

---

## 📝 Passo 2: Criar o arquivo SMBCONFIG.DAT

Agora vamos criar o arquivo de configuração para o POPStarter.

```bash
cd "/media/alace/My Passport/POPS"
nano SMBCONFIG.DAT
```

**Conteúdo** (substitua `IP_DO_SERVIDOR` pelo IP que você descobriu):

```
IP_DO_SERVIDOR 445 Drive1_1 guest
```

Exemplo: se o IP do seu servidor for `192.168.25.50`:

```
192.168.25.50 445 Drive1_1 guest
```

**Formato:** `IP PORTA COMPARTILHAMENTO USUARIO SENHA`

Como a senha não está definida, deixamos em branco (apenas o usuário `guest`).

---

## 📝 Passo 3: Criar o arquivo IPCONFIG.DAT

```bash
cd "/media/alace/My Passport/POPS"
nano IPCONFIG.DAT
```

Conteúdo (IP do PS2, Mask, Gateway):
```
192.168.25.200 255.255.255.0 192.168.25.1
```

---

## 📝 Passo 4: Verificar se o compartilhamento está acessível como guest

No seu Linux, teste se consegue acessar o compartilhamento sem senha:

```bash
smbclient //192.168.25.50/Drive1_1 -N -c "ls"
```

Substitua `192.168.25.50` pelo IP do seu servidor.

Se funcionar, vai listar as pastas (DVD, CD, POPS, etc).

Se falhar com erro de permissão, você pode precisar criar um usuário específico.

---

## 🔧 Alternativa: Criar um usuário para o POPStarter

Se `guest` não funcionar, crie um usuário específico no Samba:

```bash
# Instalar samba se não tiver
sudo apt install samba

# Criar usuário do sistema
sudo useradd -m ps2user

# Definir senha
sudo smbpasswd -a ps2user
# (escolha uma senha, ex: ps2senha)

# Adicionar ao smb.conf
sudo nano /etc/samba/smb.conf
```

Adicione no final:
```ini
[Drive1_1]
path = /media/alace/My Passport
browseable = yes
read only = no
guest ok = no
valid users = ps2user
force user = ps2user
```

Reinicie o Samba:
```bash
sudo systemctl restart smbd
```

Depois atualize o `SMBCONFIG.DAT`:
```
IP_DO_SERVIDOR 445 Drive1_1 ps2user ps2senha
```

---

## 📋 Resumo final

| Arquivo | Local | Conteúdo |
|---------|-------|----------|
| `SMBCONFIG.DAT` | `/POPS/` | `IP 445 Drive1_1 guest` |
| `IPCONFIG.DAT` | `/POPS/` | `192.168.25.200 255.255.255.0 192.168.25.1` |

---

## 🎮 Teste no PS2

1. Coloque o arquivo `SMBCONFIG.DAT` na pasta `POPS`
2. No OPL, vá para a aba **APPS** (não PS1 Games)
3. Selecione um jogo
4. Deve carregar!

---

Me diga:
1. Qual o IP do seu computador? (resultado de `hostname -I`)
2. O teste do `smbclient` funcionou?

Assim posso te ajudar a ajustar se precisar! 🚀
