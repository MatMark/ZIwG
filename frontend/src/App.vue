<template>
  <v-app>
    <AppMenu />
    <v-main>
      <router-view />
    </v-main>
  </v-app>
</template>

<script>
import AppMenu from "@/components/AppMenu.vue";
export default {
  name: "App",

  components: {
    AppMenu
  },
  data: () => ({})
};
</script>
