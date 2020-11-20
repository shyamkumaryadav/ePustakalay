<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <p>
      Hello World App
    </p>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  }
}
</script>
