import React from "react";
import Link from "next/link";
import { Camera, Handshake, Scale, Languages, ArrowRight } from "lucide-react";

export default function HomePage() {
  return (
    <div className="space-y-12 pb-16">
      {/* Hero Banner */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 pt-6">
        <div className="rounded-3xl p-8 sm:p-12 text-white shadow-xl relative overflow-hidden"
             style={{ background: "radial-gradient(circle at top right, #7A2424 0%, #5C1A1A 50%, #380C0C 100%)" }}>
          <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 items-center">
            <div className="lg:col-span-7 space-y-6">
              <span className="inline-block bg-black/30 border border-white/20 text-amber-200 text-xs px-3.5 py-1 rounded-full">
                Empowering Traditional Indian Artisans
              </span>
              <h1 className="font-serif text-4xl sm:text-5xl lg:text-6xl font-bold leading-tight">
                Your Craft.<br />
                Your Story.<br />
                <span className="text-amber-200">A Bigger Tomorrow.</span>
              </h1>
              <p className="text-stone-200 text-sm sm:text-base max-w-lg">
                An AI-powered marketplace for India&apos;s artisans to showcase, sell and grow. From village workshops directly to nationwide buyers.
              </p>
              <div className="flex flex-wrap gap-4 pt-2">
                <Link href="/add-product" className="bg-white text-kk-primary hover:bg-amber-50 font-bold px-7 py-3 rounded-full text-sm shadow-md transition">
                  Start Selling &rarr;
                </Link>
                <Link href="/marketplace" className="border border-white/40 hover:bg-white/10 text-white font-semibold px-7 py-3 rounded-full text-sm transition">
                  Explore Crafts
                </Link>
              </div>
            </div>
            <div className="lg:col-span-5">
              <div className="rounded-2xl overflow-hidden border-2 border-white/20 shadow-2xl">
                <img src="https://images.unsplash.com/photo-1606293926075-69a00dbfde81?w=800" alt="Authentic Crafts" className="w-full h-80 object-cover" />
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* 4 Value Proposition Cards */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6">
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
          <div className="bg-white border border-kk-border p-5 rounded-2xl shadow-sm space-y-2">
            <div className="w-10 h-10 rounded-xl bg-red-100 text-kk-primary flex items-center justify-center">
              <Camera className="w-5 h-5" />
            </div>
            <h3 className="font-serif font-bold text-base">AI Product Listing</h3>
            <p className="text-xs text-kk-textMuted">Turn your photos into beautiful listings.</p>
          </div>
          <div className="bg-white border border-kk-border p-5 rounded-2xl shadow-sm space-y-2">
            <div className="w-10 h-10 rounded-xl bg-orange-100 text-kk-accent flex items-center justify-center">
              <Handshake className="w-5 h-5" />
            </div>
            <h3 className="font-serif font-bold text-base">Market Linkage</h3>
            <p className="text-xs text-kk-textMuted">Connect directly with genuine buyers.</p>
          </div>
          <div className="bg-white border border-kk-border p-5 rounded-2xl shadow-sm space-y-2">
            <div className="w-10 h-10 rounded-xl bg-emerald-100 text-emerald-800 flex items-center justify-center">
              <Scale className="w-5 h-5" />
            </div>
            <h3 className="font-serif font-bold text-base">Fair Pricing</h3>
            <p className="text-xs text-kk-textMuted">Get AI-backed price suggestions.</p>
          </div>
          <div className="bg-white border border-kk-border p-5 rounded-2xl shadow-sm space-y-2">
            <div className="w-10 h-10 rounded-xl bg-purple-100 text-purple-800 flex items-center justify-center">
              <Languages className="w-5 h-5" />
            </div>
            <h3 className="font-serif font-bold text-base">Multi-Language</h3>
            <p className="text-xs text-kk-textMuted">List in your language, reach nationwide.</p>
          </div>
        </div>
      </section>
    </div>
  );
}
