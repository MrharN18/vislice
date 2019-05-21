<!DOCTYPE html>
<html>

<body>

  <h1>Vislice</h1>

  <blockquote>
    {{ igra.pravilni_del_gesla() }}
  </blockquote>


  <form action="/igra/" method="POST">
   <input type="text" name="poskus">
    <input type="submit" value="Ugibaj">
  </form>

  <img src="vislice/img/0.jpg" alt="obesanje">

  <form action="/igra/" method="post">
    <button type="submit">Nova igra</button>
  </form>
</body>

</html>