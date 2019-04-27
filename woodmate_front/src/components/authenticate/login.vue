<template>
  <div class="container-fulid wrapper">
    <div class="row">
      <div class="col">
        <div class="container" id="authen-form">
          <h1>Login</h1>
          <div class="choice">
            <button id="facebook">
              <i class="fab fa-facebook-f"></i> | Login with Facebook
            </button>
            <button id="google">
              <i class="fab fa-google"></i> | Login with Google account
            </button>
          </div>
          <p>- OR -</p>
          <br>
          <form>
            <div class="form-group">
              <input
                type="email"
                class="form-control"
                id="exampleInputEmail1"
                aria-describedby="emailHelp"
                placeholder="Email"
              >
            </div>
            <div class="form-group">
              <input
                type="password"
                class="form-control"
                id="exampleInputPassword1"
                placeholder="Password"
              >
            </div>
            <div class="form-group form-check">
              <span id="remember">
                <input type="checkbox" class="form-check-input" id="exampleCheck1">
                <label class="form-check-label" for="exampleCheck1">Remember me</label>
              </span>
              <router-link to="/" id="forget">Forgot Password?</router-link>
            </div>
            <br>
            <button type="submit" class="btn btn-primary btn-block" id="submit">Submit</button>
          </form>
        </div>
      </div>
      <div class="col" id="frame1">
        <img
          src="https://static.dezeen.com/uploads/2018/02/voice-stockholm-design-week-furniture-dezeen-sq.jpg"
          alt
        >
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "login",
  data() {
    return {};
  }
};
</script>

<style>
input[type="checkbox"] {
  background: transparent;
  border: 1px solid black;
}
.wrapper {
  width: 100vw;
  height: 100vh;
  overflow: hidden;
}
#authen-form {
  padding: 10em;
}
img {
  width: 100%;
  /* transform: translateY(-30vh);  */
  position: absolute;
  left: 0px;
  top: 0px;
  z-index: -10;
}
#frame1 {
  padding-top: 15vh;
  margin: 0 auto;
  position: relative;
  height: 100vh;
  overflow: hidden;
}
#remember {
  float: left;
}
.choice {
  margin: 2em 0;
  display: flex;
  align-items: center;
  justify-content: center;
}
.choice > button {
  margin: 0 2em;
  padding: 0.5em 1.5em;
  border: none;
  color: rgb(241, 241, 241);
}

.choice > button > i {
  color: white;
}
#facebook {
  background: #4267b2;
}
#google {
  background: #ea4335;
}
#forget {
  float: right;
}
#submit{
    margin-top: 1em;
}
</style>
