<template>
  <div class="hello">
    <md-whiteframe>
      <md-toolbar md-theme="blue">
        <span class="md-title">My app dashboard</span>
      </md-toolbar>
    </md-whiteframe>

    <md-layout md-gutter="24" md-align="center">
      <md-layout md-flex="35">
        <md-card md-with-hover>
          <md-card-header>
            <div class="md-title">Title goes here</div>
            <div class="md-subhead">Subtitle here</div>
          </md-card-header>

          <md-card-content>
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Optio itaque ea, nostrum odio. Dolores, sed
            accusantium quasi non, voluptas eius illo quas, saepe voluptate pariatur in deleniti minus sint. Excepturi.
          </md-card-content>

          <md-card-actions>
            <md-button>Action</md-button>
            <md-button>Action</md-button>
          </md-card-actions>
        </md-card>
      </md-layout>

      <md-layout md-flex="35">
        <md-card md-with-hover>
          <md-card-header>
            <div class="md-title">Title goes here</div>
            <div class="md-subhead">Subtitle here</div>
          </md-card-header>

          <md-card-content>
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Optio itaque ea, nostrum odio. Dolores, sed
            accusantium quasi non, voluptas eius illo quas, saepe voluptate pariatur in deleniti minus sint. Excepturi.
          </md-card-content>

          <md-card-actions>
            <md-button>Action</md-button>
            <md-button>Action</md-button>
          </md-card-actions>
        </md-card>
      </md-layout>
    </md-layout>

  </div>
</template>

<script>
  export default {
    name: 'hello',
    data () {
      return {
        msg: 'Welcome to Your Vue.js App'
      }
    }
  }
</script>

<style scoped>
  .md-card {
    margin-top: 10px;
  }
</style>
