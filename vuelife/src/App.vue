<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/gameoflifetext.gif">
    <LifeGame/>
  </div>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'
import LifeGame from './components/LifeGame.vue'

export default {
  name: 'App',
  components: {
    LifeGame
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

html {
  background-color: #1b1b1b;
}

</style>
