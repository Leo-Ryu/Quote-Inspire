package com.ryustudios.quoteinspire

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.os.Handler
import androidx.core.content.ContextCompat
import com.google.gson.annotations.SerializedName
import io.reactivex.Observable
import io.reactivex.android.schedulers.AndroidSchedulers
import io.reactivex.disposables.Disposable
import io.reactivex.schedulers.Schedulers
import kotlinx.android.synthetic.main.activity_main.*
import retrofit2.http.GET
import retrofit2.converter.gson.GsonConverterFactory
import retrofit2.Retrofit
import retrofit2.adapter.rxjava2.RxJava2CallAdapterFactory
import androidx.swiperefreshlayout.widget.SwipeRefreshLayout


const val BASE_URL = "http://lryu.pythonanywhere.com/"

class MainActivity : AppCompatActivity(), SwipeRefreshLayout.OnRefreshListener {

    private var mSwipeRefreshLayout: SwipeRefreshLayout? = null

    private val quoteApiServe by lazy {
        QuoteApiService.create()
    }
    var disposable: Disposable? = null

    override fun onCreate(savedInstanceState: Bundle?) {
        setContentView(R.layout.activity_main)

        mSwipeRefreshLayout = swipeToRefresh
        mSwipeRefreshLayout?.setOnRefreshListener(this)

        super.onCreate(savedInstanceState)

        QI.setTextColor(ContextCompat.getColor(applicationContext, R.color.colorPrimaryDark))
        fetchQuote()
    }

    override fun onPause() {
        super.onPause()
        disposable?.dispose()
    }

    private fun fetchQuote() {
        disposable = quoteApiServe.fetchQuote()
            .subscribeOn(Schedulers.io())
            .observeOn(AndroidSchedulers.mainThread())
            .subscribe {
                    result ->
                quoteText.text = result[0].quote
                quoteText.setTextColor(ContextCompat.getColor(applicationContext, R.color.colorPrimary))
                authorText.text = result[0].author
                authorText.setTextColor(ContextCompat.getColor(applicationContext, R.color.colorAccent))

            }

        if (mSwipeRefreshLayout!!.isRefreshing) {
            mSwipeRefreshLayout?.isRefreshing = false
        }
    }

    override fun onRefresh() {
        fetchQuote()
        Handler().postDelayed(Runnable { mSwipeRefreshLayout?.setRefreshing(false) }, 2000)
    }
}

data class QuoteModel (
    @SerializedName("id") val id: Int,
    @SerializedName("quote") val quote: String,
    @SerializedName("author") val author: String
)

interface QuoteApiService {

    @GET("quote/")
    fun fetchQuote(): Observable<List<QuoteModel>>


    companion object {
        fun create(): QuoteApiService {
            val retrofit = Retrofit.Builder()
                .baseUrl(BASE_URL)
                .addConverterFactory(GsonConverterFactory.create())
                .addCallAdapterFactory(RxJava2CallAdapterFactory.create())
                .build()

            return retrofit.create(QuoteApiService::class.java)
        }
    }
}



