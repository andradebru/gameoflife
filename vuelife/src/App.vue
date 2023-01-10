<template>
  <div id="app">
    <img alt="Game of Life shining colorful title" src="./assets/gameoflifetext.gif">
    <LifeGame/>
  </div>
</template>

<script>
import LifeGame from './components/LifeGame.vue'

export default {
  name: 'App',
  components: {
    LifeGame
  }
}
</script>

<style>
img {
  box-sizing: border-box;
  width: 20rem;
  margin-top: 60px;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

html {
  box-sizing: border-box;
  height: 100vh;
  width: 100vw;
  background-color: #f8f4ef;
}

</style>
