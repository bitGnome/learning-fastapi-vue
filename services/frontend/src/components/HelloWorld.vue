<template>
  <div>
    <p>{{ msg }}</p>
  </div>
</template>

<script>
  import axios from 'axios'
  
  export default {
    name: 'Ping',
    data () {
      return {
        msg: 'Hello World!'
      }
    },
    methods: {
      getMessage () {
        axios.get('/')
          .then((response) => {
            this.msg = response.data
          })
          .catch((error) => {
            console.error(error)
          })
      }
    },
    created() {
      this.getMessage()
    }
  }
</script>