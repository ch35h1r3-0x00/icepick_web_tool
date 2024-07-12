<h4 align="center">
  <pre>
$$$$$$\  $$$$$$\  $$$$$$$$\           $$\           $$\       
\__$$  _|$$  __$$\ $$  _____|          \__|          $$ |      
   $$ |  $$ /  \__|$$ |       $$$$$$\  $$\  $$$$$$$\ $$ |  $$\ 
   $$ |  $$ |      $$$$$\    $$  __$$\ $$ |$$  _____|$$ | $$  |
   $$ |  $$ |      $$  __|   $$ /  $$ |$$ |$$ /      $$$$$$  / 
   $$ |  $$ |  $$\ $$ |      $$ |  $$ |$$ |$$ |      $$  _$$<  
   $$$$$$\ \$$$$$$  |$$$$$$$$\ $$$$$$$  |$$ |\$$$$$$$\ $$ | \$$\ 
   \______| \______/ \________|$$  ____/ \__| \_______|\__|  \__|
                               $$ |                              
                               $$ |                              
\__|
  </pre>
</h4>

<p align="center">
  Icepick Web Tool é um conjunto básico de ferramentas para reconhecimento e escaneamento web.
</p>

<p align="center">
  O código possui 6 wordlists (padrão e comuns), que podem ser alteradas de acordo com as necessidades do usuário.
  Ao iniciar, o código solicita uma URL e segue a ordem abaixo para suas atividades:
</p>

<ul>
  <li>banner grab</li>
  <li>resolver</li>
  <li>netblock</li>
  <li>subdomain bruteforce</li>
  <li>directories bruteforce</li>
  <li>php bruteforce</li>
  <li>nmap scan</li>
</ul>

<h2>Modo de Uso:</h2>

<p>Execute o seguinte comando:</p>

<pre><code>sudo python3 icepick.py
</code></pre>

<p>A URL deve ser inserida no formato:</p>

<pre><code>http://example.com/
ou
https://example.com/
sem "www"
</code></pre>

<p>O código possui 7 scripts que podem ser usados independentemente, com exceção de iceban.py, que não pede argumentos, pois funciona com entrada interativa.</p>

<h2>Modo de Uso dos Scripts Individuais:</h2>

<p>Execute o script com o seguinte formato:</p>

<pre><code>python3 scriptname.py argument
</code></pre>

<p>Para usar o código com uma wordlist mais extensa em icedir.py e icephp.py, podemos comentar a linha contendo "--common" e descomentar a próxima linha no código:</p>

<pre><code># icedir = execute_subprocess(["python3", path_icedir, "--common", tempurl])
# descomente a linha abaixo para usar a maior wordlist
icedir = execute_subprocess(["python3", path_icedir, tempurl])
</code></pre>

<p>No código icescan.py, os parâmetros do nmap podem ser alterados ou adicionados nas seções abaixo:</p>

<pre><code>if option == 1:
    scan_types = ["-sT", "--top-ports=10000"]
    output_suffix = "nmapTCP10000"
elif option == 2:
    scan_types = ["-sT", "-sV", "-O", "--top-ports=10000"]
    output_suffix = "nmapTCP10000_full"
elif option == 3:
    scan_types = ["-sT", "-p-"]
    output_suffix = "nmapTCP_all"
elif option == 4:
    scan_types = ["-sU", "--top-ports=1000"]
    output_suffix = "nmapUDP1000"
elif option == 5:
    scan_types = ["-sU", "-sV", "-O", "--top-ports=1000"]
    output_suffix = "nmapUDP1000_full"
elif option == 6:
    scan_types = ["-sU", "-p-"]
    output_suffix = "nmapUDP_all"
elif option == 7:
    scan_types = ["-sS", "-p-", "--open"]
    output_suffix = "nmap_all"
elif option == 8:
    scan_types = ["-sS", "-O", "-sV", "-p-", "--script=vuln"]
    output_suffix = "nmap_aggressive"
</code></pre>

<p><strong>Obs:</strong> O código sempre criará 3 arquivos:</p>

<ul>
  <li>tempurl.txt: contém a URL usada pelo icepick.py.</li>
  <li>tempip.txt: contém o IP usado pelo icepick.py.</li>
  <li>target.txt: contém as informações obtidas durante a execução.</li>
</ul>

