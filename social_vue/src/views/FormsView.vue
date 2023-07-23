<template>
    <form v-on:submit.prevent="submitForm" method="post">
        <div class="w-full max-w-4xl mx-auto p-5">
            <div class=" grid gap-6 mb-6 md:grid-cols-2">
                <div>
                    <label for="title" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Title</label>
                    <input v-model="title" type="text" id="title"
                        class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                        placeholder="Title..." required>
                </div>
                <div>
                    <label for="summary"
                        class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Summary</label>
                    <input v-model="summary" type="text" id="summary"
                        class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                        placeholder="Summary..." required>
                </div>
            </div>
            <div class="w-full mb-4 border border-gray-200 rounded-lg bg-gray-50 dark:bg-gray-700 dark:border-gray-600">
                <div class="px-4 py-2 bg-white rounded-t-lg dark:bg-gray-800">
                    <label for="comment" class="sr-only">Your comment</label>
                    <textarea v-model="body" id="comment" rows="4"
                        class="w-full px-0 text-sm text-gray-900 bg-white border-0 dark:bg-gray-800 focus:ring-0 dark:text-white dark:placeholder-gray-400"
                        placeholder="Write a comment..." required></textarea>
                </div>
                <div class="flex items-center justify-between px-3 py-2 border-t dark:border-gray-600">
                    <button type="submit"
                        class="inline-flex items-center py-2.5 px-4 text-xs font-medium text-center text-white bg-blue-700 rounded-lg focus:ring-4 focus:ring-blue-200 dark:focus:ring-blue-900 hover:bg-blue-800">
                        Post comment
                    </button>
                    <div class="flex pl-0 space-x-1 sm:pl-2">
                        <p class="inline-flex justify-center items-center text-gray-500">
                            Upload image
                        </p>
                        <button type="button"
                            class="inline-flex justify-center items-center p-2 text-gray-500 rounded cursor-pointer hover:text-gray-900 hover:bg-gray-100 dark:text-gray-400 dark:hover:text-white dark:hover:bg-gray-600">
                            <svg class="w-4 h-4" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor"
                                viewBox="0 0 20 18">
                                <path
                                    d="M18 0H2a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2Zm-5.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3Zm4.376 10.481A1 1 0 0 1 16 15H4a1 1 0 0 1-.895-1.447l3.5-7A1 1 0 0 1 7.468 6a.965.965 0 0 1 .9.5l2.775 4.757 1.546-1.887a1 1 0 0 1 1.618.1l2.541 4a1 1 0 0 1 .028 1.011Z" />
                            </svg>
                            <span class="sr-only">Upload image</span>
                        </button>
                    </div>
                </div>
            </div>
        </div>

    </form>
</template>


<script>
import axios from 'axios'
import { useToastStore } from '@/stores/toast'


export default {
    setup() {
        const toastStore = useToastStore()

        return {
            toastStore
        }
    },

    data() {
        return {
            posts: [],
            title: '',
            summary: '',
            body: '',
        }
    },

    methods: {
        submitForm() {
            console.log('submitForm', this.title, this.summary, this.body)

            axios
                .post('/api/posts/create/', {
                    'title': this.title,
                    'summary': this.summary,
                    'body': this.body
                })
                .then(response => {
                    this.posts.unshift(response.data)
                    this.title = ''
                    this.summary = ''
                    this.body = ''
                    this.toastStore.showToast(5000, 'The post successfully created!', 'bg-emerald-300')
                })
                .catch(error => {
                    console.log('error', error)
                })
        }
    }
}
</script>