<h1>What to accomplish</h1>
provide simple and easy MQTT service over a website using javascript Paho
<h1>thoughts process</h1>
<ol>
<li>first I read about MQTT protocol</li>
<li>thought about building a web application using Flask that connects to the broker and sends the result to the client,
 I mean the  server handles all requests to the broker</li> 
<li>I found out that the methodology will be slow and a much easier way is to make 
all functionalities at client side with javascript Paho library</li>
</ol>
<h1>developing process</h1>
<ol>
<li>as this is the first time I use this library I used the documentation<a href="http://www.eclipse.org/paho/files/jsdoc/Paho.MQTT.Client.html">
paho_doc</a></li>
<li>I tried to provide all essential functionalities like connect 
with the broker using host and port only with hardcoded data</li>
<li>
use jquery to use user entered data instead of hardcoded data</li>
<li>added rest of other functionalities like use username and password and retain message</li>
</ol>
<h1>Previous experience</h1>
I consider myself intermediate to expert with Flask as I used it in 3 projects one of them was in an internship where I built an API and it was a big project that took me 3 months of continuous work an