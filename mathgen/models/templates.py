card_front = '''
             <script>
             // v0.5.2 - https://github.com/SimonLammer/anki-persistence/blob/3912637b7a53cfe8357f3946d0255804386ac43c/script.js
             if(void 0===window.Persistence){var _persistenceKey="github.com/SimonLammer/anki-persistence/",_defaultKey="_default";if(window.Persistence_sessionStorage=function(){var e=!1;try{"object"==typeof window.sessionStorage&&(e=!0,this.clear=function(){for(var e=0;e<sessionStorage.length;e++){var t=sessionStorage.key(e);0==t.indexOf(_persistenceKey)&&(sessionStorage.removeItem(t),e--)}},this.setItem=function(e,t){void 0==t&&(t=e,e=_defaultKey),sessionStorage.setItem(_persistenceKey+e,JSON.stringify(t))},this.getItem=function(e){return void 0==e&&(e=_defaultKey),JSON.parse(sessionStorage.getItem(_persistenceKey+e))},this.removeItem=function(e){void 0==e&&(e=_defaultKey),sessionStorage.removeItem(_persistenceKey+e)})}catch(e){}this.isAvailable=function(){return e}},window.Persistence_windowKey=function(e){var t=window[e],i=!1;"object"==typeof t&&(i=!0,this.clear=function(){t[_persistenceKey]={}},this.setItem=function(e,i){void 0==i&&(i=e,e=_defaultKey),t[_persistenceKey][e]=i},this.getItem=function(e){return void 0==e&&(e=_defaultKey),t[_persistenceKey][e]||null},this.removeItem=function(e){void 0==e&&(e=_defaultKey),delete t[_persistenceKey][e]},void 0==t[_persistenceKey]&&this.clear()),this.isAvailable=function(){return i}},window.Persistence=new Persistence_sessionStorage,Persistence.isAvailable()||(window.Persistence=new Persistence_windowKey("py")),!Persistence.isAvailable()){var titleStartIndex=window.location.toString().indexOf("title"),titleContentIndex=window.location.toString().indexOf("main",titleStartIndex);titleStartIndex>0&&titleContentIndex>0&&titleContentIndex-titleStartIndex<10&&(window.Persistence=new Persistence_windowKey("qt"))}}
             </script>

             <div id="problem">{{Problem}}</div>

             <script>
                function getRandomInt(min, max) {
                    min = Math.ceil(min);
                    max = Math.floor(max);
                    return Math.floor(Math.random() * (max - min + 1)) + min;
                }
			    var problem = document.getElementById("problem").innerHTML;
                var map = {};
                var regexp = /\{\{\s*\m\d+\s*\:\:\s*\d+\s*\-\s*\d+\s*\}\}/g;
                var variables = problem.match(regexp);
                
                variables.forEach(v => {
                    regexp = /\d+-\d+/g;
                    var range = v.match(regexp)[0].split("-");
                    regexp = /(\m\d+)+/g;
                    variable = v.match(regexp)[0];
                    var random = getRandomInt(parseInt(range[0]), parseInt(range[1]));
                    map[variable] = random;
                    problem = problem.replace(v, random);
                });
				document.getElementById("problem").innerHTML = problem;
                if (Persistence.isAvailable()) {  // Check whether Persistence works on the client.
                    Persistence.setItem("problem", problem);
                    Persistence.setItem("map", JSON.stringify(map));
                }
            </script>
            '''

card_back = '''
            <script type=“text/javascript”>
            // v0.5.2 - https://github.com/SimonLammer/anki-persistence/blob/3912637b7a53cfe8357f3946d0255804386ac43c/script.js
            if(void 0===window.Persistence){var _persistenceKey="github.com/SimonLammer/anki-persistence/",_defaultKey="_default";if(window.Persistence_sessionStorage=function(){var e=!1;try{"object"==typeof window.sessionStorage&&(e=!0,this.clear=function(){for(var e=0;e<sessionStorage.length;e++){var t=sessionStorage.key(e);0==t.indexOf(_persistenceKey)&&(sessionStorage.removeItem(t),e--)}},this.setItem=function(e,t){void 0==t&&(t=e,e=_defaultKey),sessionStorage.setItem(_persistenceKey+e,JSON.stringify(t))},this.getItem=function(e){return void 0==e&&(e=_defaultKey),JSON.parse(sessionStorage.getItem(_persistenceKey+e))},this.removeItem=function(e){void 0==e&&(e=_defaultKey),sessionStorage.removeItem(_persistenceKey+e)})}catch(e){}this.isAvailable=function(){return e}},window.Persistence_windowKey=function(e){var t=window[e],i=!1;"object"==typeof t&&(i=!0,this.clear=function(){t[_persistenceKey]={}},this.setItem=function(e,i){void 0==i&&(i=e,e=_defaultKey),t[_persistenceKey][e]=i},this.getItem=function(e){return void 0==e&&(e=_defaultKey),t[_persistenceKey][e]||null},this.removeItem=function(e){void 0==e&&(e=_defaultKey),delete t[_persistenceKey][e]},void 0==t[_persistenceKey]&&this.clear()),this.isAvailable=function(){return i}},window.Persistence=new Persistence_sessionStorage,Persistence.isAvailable()||(window.Persistence=new Persistence_windowKey("py")),!Persistence.isAvailable()){var titleStartIndex=window.location.toString().indexOf("title"),titleContentIndex=window.location.toString().indexOf("main",titleStartIndex);titleStartIndex>0&&titleContentIndex>0&&titleContentIndex-titleStartIndex<10&&(window.Persistence=new Persistence_windowKey("qt"))}}
            </script>
            <div id="front">{{Problem}}</div>

            <hr id=answer>

            <div id="solution">{{Solution}}</div>

            <script>
            function decodeHtml(html) {
                var txt = document.createElement("textarea");
                txt.innerHTML = html;
                return txt.value
            }
            if (Persistence.isAvailable()) {  // Check whether Persistence works on the client.
                var problem = Persistence.getItem("problem"); // Retrieve the previously stored number and override the default.
                var map = JSON.parse(Persistence.getItem("map"));
                Persistence.clear();            // Clear the storage, so a new random number will be created on the next card.
            }
			var solution = document.getElementById("solution").innerHTML;
			for (var v in map) {
				solution = solution.replace(v, map[v])
			}
			document.getElementById("front").innerHTML = problem;
			document.getElementById("solution").innerHTML = eval(decodeHtml(solution));
            </script>
            '''