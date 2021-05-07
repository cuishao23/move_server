<template>
  <div>
    <ul id="mainMenu">
      <li class="level1 no-children">
        <router-link :to="{name:'usernumber'}" @click.native="show = 'usernumber'">用户信息</router-link>
      </li>
    </ul>
  </div>
</template>

<script>
  // import Event from '../../assets/event.js';

  export default {
    name: "menucontainer",
    data() {
      return {
        show: 'baseinfo',
      };
    },
    activated: function() {
      let to = this.$route.fullPath;
      this.path_event(to)
    },
    methods: {
    }
  }
</script>

<style scoped>
  .level2 li a.router-link-active, .no-children .router-link-active {
    background: #53afe4;
    color: white;
  }

  .children-active {
    font-weight: 700;
    color: #000000 !important;
    background: white;
  }
</style>
