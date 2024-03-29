# Autogenerated file
def render(*a, **d):
    yield """<!DOCTYPE html>
<html lang=\"en\">
  <head>
    <meta charset=\"UTF-8\" />
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\" />
    <meta http-equiv=\"X-UA-Compatible\" content=\"ie=edge\" />
    
    <title>Dashboard</title>
    <link
      href=\"https://unpkg.com/boxicons@2.0.7/css/boxicons.min.css\"
      rel=\"stylesheet\"
    />
    <link rel=\"stylesheet\" href=\"static/style.css\" />
    <script src=\"https://cdn.plot.ly/plotly-2.16.1.min.js\"></script>
    <style>html """
    yield """{ font-family: Helvetica; display: inline-block; margin: 0px auto; text-align: center;}
      .buttonGreen """
    yield """{ background-color: #4CAF50; border: 2px solid #000000;; color: white; padding: 15px 32px; text-align: center; text-decoration: none; display: inline-block; font-size: 16px; margin: 4px 2px; cursor: pointer; }
      .buttonRed """
    yield """{ background-color: #D11D53; border: 2px solid #000000;; color: white; padding: 15px 32px; text-align: center; text-decoration: none; display: inline-block; font-size: 16px; margin: 4px 2px; cursor: pointer; }
      .buttonBlue"""
    yield """{ background-color: #0000FF; border: 2px solid #000000;; color: white; padding: 15px 32px; text-align: center; text-decoration: none; display: inline-block; font-size: 16px; margin: 4px 2px; cursor: pointer; }
      .tomorrow """
    yield """{
 
          width: 336px;
         
        }
      text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}
    </style>
  </head>
  <body>
    <div class=\"sidebar\">
      <div class=\"logo-details\">
        <i class='bx bx-microchip'></i>
        <span class=\"logo_name\">RP IOT</span>
      </div>
      <ul class=\"nav-links\">
        <li>
          <a href=\"/\" class=\"active\">
            <i class=\"bx bx-grid-alt\"></i>
            <span class=\"links_name\">Dashboard</span>
          </a>
        </li>
      </ul>
    </div>
    <section class=\"home-section\">
      <nav>
        <div class=\"sidebar-button\">
          <i class=\"bx bx-menu sidebarBtn\"></i>
          <span class=\"dashboard\">Dashboard</span>
        </div>
      </nav>
      <div class=\"home-content\">
        <div class=\"overview-boxes\">
          <div class=\"box\">
            <div class=\"right-side\">
              <div class=\"box-topic\">Data si ora:</div>
              <p id=\"datetime\"></p>

                  <script>
                    var now = new Date();
                    var datetime = now.toLocaleString();
                    document.getElementById(\"datetime\").innerHTML = datetime;
                  </script>
              <div class=\"number\" id=\"temperature\"></div>
            </div>
           
          </div>

            
             
                  <script>
                          (function(d, s, id) """
    yield """{
                              if (d.getElementById(id)) """
    yield """{
                                  if (window.__TOMORROW__) """
    yield """{
                                      window.__TOMORROW__.renderWidget();
                                  }
                                  return;
                              }
                              const fjs = d.getElementsByTagName(s)[0];
                              const js = d.createElement(s);
                              js.id = id;
                              js.src = \"https://www.tomorrow.io/v1/widget/sdk/sdk.bundle.min.js\";

                              fjs.parentNode.insertBefore(js, fjs);
                          })(document, 'script', 'tomorrow-sdk');
                          </script>

                          <div class=\"tomorrow\"
                             data-location-id=\"\"
                             data-language=\"EN\"
                             data-unit-system=\"METRIC\"
                             data-skin=\"light\"
                             data-widget-type=\"aqiMini\"
                             
                          >

                          </div>
              
            
           

          <div >
            <div class=\"right-side\">
              <div class=\"box-topic\"></div>

            </div>

          </div>
          <div >
            <div class=\"right-side\">
              <div class=\"box-topic\"></div>

            </div>
           
          </div>
        </div>
        <div class=\"graph-box\">
          <div class=\"history-charts\">
            <div class=\"title\">Lights</div>
              <form action = \"/leds\" method = \"POST\"><center>
                <label for = \"Name\">Introdu pin ul de iesire:</label>
                <input type= \"text\" name=\"name\" id= \"name\">
                <br>
                 <label for = \"Name\">Introdu pin ul de intrare:</label>
                <input type= \"text\" name=\"name_in\" id= \"name\">
                <center> <button class=\"buttonBlue\" name=\"led\" type=\"submit\">SUBMIT</button>
              </form>
              

            </div>
          </div>
          
        </div>
      </div>
    </section>
    <script src=\"static/main.js\"></script>
  </body>
</html>
"""
