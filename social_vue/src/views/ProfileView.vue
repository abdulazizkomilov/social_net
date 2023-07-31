<template>
    <div>
        <header>
        </header>
        <main>
            <div class="row">
                <div class="left col-lg-4">
                    <h2 class="text-2xl">
                        {{ userStore.user.name }} <span
                            class="bg-gray-100 text-gray-800 text-xs font-medium mr-2 px-2.5 py-0.5 rounded dark:bg-gray-700 dark:text-gray-300">UI/UX
                            Designer</span>
                    </h2>
                    <p>{{ userStore.user.email }}</p>
                    <div>
                        <span
                            class="bg-green-100 text-green-800 text-xs font-medium mr-2 px-2.5 py-0.5 rounded-full cursor-pointer dark:bg-green-900 dark:text-green-300">Follow</span>
                        <span
                            class="bg-purple-100 text-purple-800 text-xs font-medium mr-2 px-2.5 py-0.5 rounded-full cursor-pointer dark:bg-purple-900 dark:text-purple-300">Request</span>
                    </div>
                    <div class="stats row flex">
                        <div class="stat col-xs-4" style="padding-right: 50px;">
                            <p class="number-stat">3,619</p>
                            <p class="desc-stat">Followers</p>
                        </div>
                        <div class="stat col-xs-4">
                            <p class="number-stat">42</p>
                            <p class="desc-stat">Following</p>
                        </div>
                        <div class="stat col-xs-4" style="padding-left: 50px;">
                            <p class="number-stat">38</p>
                            <p class="desc-stat">Uploads</p>
                        </div>
                    </div>
                    <p class="desc">Hi ! My name is Jane Doe. I'm a UI/UX Designer from Paris, in France. I really enjoy
                        photography and mountains.</p>
                </div>
                <div class="w-full max-w-2xl mx-auto p-5">
                    <div class="divide-y divide-gray-200 dark:divide-gray-700">
                        <article class="py-6" v-for="post in posts" v-bind:key="post.id">
                            <div class="flex items-center justify-between mb-3 text-gray-500">
                                <div>
                                    <a class="bg-blue-100 text-blue-800 text-sm font-medium mr-2 px-2.5 py-0.5 rounded dark:bg-blue-200 hover:bg-blue-200 dark:hover:bg-blue-300 dark:text-blue-800 mb-2"
                                        href="/blog/tag/laravel/">
                                        #Laravel
                                    </a>
                                </div>
                                <span class="text-xs">
                                    Published
                                    <time>
                                        {{ post.created_at_formatted }} ago
                                    </time>
                                </span>
                            </div>
                            <h3 class="mb-2 text-lg font-bold tracking-tight text-gray-900 dark:text-white hover:italic">
                                <a href="">
                                    {{ post.title }}
                                </a>
                            </h3>
                            <div class="py-5">
                                <a href="#">
                                    <img class="rounded-2xl"
                                        style="display: block; margin-left: auto; margin-right: auto; width: 60%;"
                                        src="../assets/mac.jpeg" alt="" />
                                </a>
                            </div>
                            <p class="mb-5 text-sm text-gray-500 dark:text-gray-400">
                                {{ post.summary }}
                            </p>

                            <div class="flex items-center justify-between">
                                <a class="flex items-center space-x-2" href="/blog/author/rich/">
                                    <img class="rounded-full w-7 h-7"
                                        src="https://publisher.flowbite.com/content/images/2023/01/1605304654466.jpg"
                                        alt="Rich Klein profile picture">
                                    <span class="font-medium dark:text-white">
                                        {{ post.created_by.name }}
                                    </span>
                                </a>
                                <a class="inline-flex items-center font-medium text-blue-600 hover:underline dark:text-blue-500"
                                    href="/blog/how-to-use-flowbite-ui-components-with-laravel-and-alpine-js/">
                                    Read more
                                    <svg class="w-4 h-4 ml-2" fill="currentColor" viewBox="0 0 20 20"
                                        xmlns="http://www.w3.org/2000/svg">
                                        <path fill-rule="evenodd"
                                            d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z"
                                            clip-rule="evenodd"></path>
                                    </svg>
                                </a>
                            </div>
                        </article>
                    </div>
                </div>
            </div>
        </main>
    </div>
</template>


<script>
import axios from 'axios'
import { useUserStore } from '@/stores/user'

export default {
    setup() {
        const userStore = useUserStore()

        return {
            userStore
        }
    },

    name: 'FeedView',

    data() {
        return {
            posts: [],
        }
    },

    mounted() {
        this.getFeed()
    },

    methods: {
        getFeed() {
            axios
                .get('/api/posts/')
                .then(response => {
                    console.log('data', response.data)

                    this.posts = response.data
                })
                .catch(error => {
                    console.log('error', error)
                })
        },
    }
}
</script>